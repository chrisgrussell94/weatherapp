from flask import Flask, render_template, request, abort
import json
import urllib.request

app = Flask(__name__)


def celcius(temp):
    return str(round(float(temp) - 273.16, 2))

def farenheiht(temp):
    return str(round((float(temp) - 273.16) * 1.8 +32))


@app.route('/', methods=['POST', 'GET'])
def weather():
    api_key = '13bc68f0e62abb2df7b6c6c75208b714'
    if request.method == 'POST':
        city = request.form['city']
    else:

        city = 'sikeston'

    try:
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key).read()
    except:
        return abort(404)


    alldata = json.loads(source)

    data = {
        "country_code": str(alldata['sys']['country']),
        "coordinate": str(alldata['coord']['lon']) + ' ' + str(alldata['coord']['lat']),
        "temp": str(alldata['main']['temp']) + 'k',
        "temp_far": farenheiht(alldata['main']['temp']) + 'F',
        "pressure": str(alldata['main']['pressure']),
        "humidity": str(alldata['main']['humidity']),
        "cityname": str(city),
    }
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)