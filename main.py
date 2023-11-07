from flask import Flask, render_template, request, make_response
from api import api_calls

app = Flask(__name__)  # Flask constructor

@app.route("/")
def index():
   return render_template("index.html")

@app.route('/search-location', methods = ['POST', 'GET'])
def search_location():
    if request.method == 'POST':
        location = request.form['location']
    list = api_calls.listLocations(location)
    message = ""
    if len(list) == 0:
        message = 'No results were found for the location "{}"'.format(location)

    return render_template("index.html", location = location, list = list, message = message)

@app.route('/forecast', methods = ['POST', 'GET'])
def forecast():
    if request.method == 'POST':
        location = request.form['hlocation']
        coordinates = request.form['coordinates']
        latitude = coordinates.split(';')[0]
        longitude = coordinates.split(';')[1]
        weather = api_calls.forecast(latitude, longitude)

        message = ""
        if 'error' in weather:
            message = "Error: {}".format(weather['reason'])
            weather = None

        return render_template("index.html", location = location, weather = weather, message = message)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()