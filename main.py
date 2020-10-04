from flask import Flask, render_template, request, abort
import json
import urllib.request

app = Flask(__name__)


def farenheit(temp):
    return str(round((float(temp) - 273.16) * 1.8 + 32))


@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'Sikeston'
    try:
        api_request = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=13bc68f0e62abb2df7b6c6c75208b714').read()
    except:
        abort(404)

    alldata = json.loads(api_request)
    info = {
        "temp_far": farenheit(alldata['main']['temp']) + 'F',
        "pressure": str(alldata['main']['pressure']),
        "humidity": str(alldata['main']['humidity']),
        "cityname": str(city),
        "description": str(alldata['weather'][0]['description'])
    }
    return render_template('index.html', data=info)


if __name__ == '__main__':
    app.run(debug=True)
