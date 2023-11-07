import requests

api_loc_url = "https://geocode.maps.co/search?q={}"
api_weather_url = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current=temperature_2m,relativehumidity_2m,apparent_temperature,windspeed_10m&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"

def listLocations(input_text):
    list = []
    response = requests.get(api_loc_url.format(input_text))
    for item in response.json():
        list.append(item)
    return list

def forecast(latitude, longitude):
    response = requests.get(api_weather_url.format(latitude, longitude))
    return response.json()