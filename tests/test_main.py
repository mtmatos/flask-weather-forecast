import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_search_location():
    client = app.test_client()

    # Trying to search for a non-existing location, must return a no results message
    response = client.post("/search-location", data={
        "location": "Xanadu Shangrila"
    })
    assert response.status_code == 200
    assert b"No results" in response.data

    # Trying to search a valid location, must return a list for selection
    response = client.post("/search-location", data={
        "location": "Belem"
    })
    assert b"Select a location:" in response.data

def test_forecast():
    client = app.test_client()

    # Trying to pass no data, must return error
    response = client.post("/forecast", data={})
    assert response.status_code == 400

    # Trying to pass invalid coordinates must return error
    response = client.post("/forecast", data={
        'hlocation': 'Belem',
        'coordinates': '0;314159265'
    })
    assert response.status_code == 200
    assert b"Error:" in response.data

    # Passing valid data, must return the weather conditions
    response = client.post("/forecast", data={
        'hlocation': 'Belem',
        'coordinates': '-1.45056;-48.4682453'
    })
    assert response.status_code == 200
    assert b"Current weather conditions" in response.data