from flask import Flask, render_template, request
import json
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    
        api = '9f7bd6b5543662153f6a5a579b3cd79b'  # key authenticate to openweather api
        # Corrected URL formatting without extra space
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, api)
        source = urllib.request.urlopen(url).read()
        list_of_data = json.loads(source)
        data = {
            'city':city,
            'country_code': str(list_of_data['sys']['country']),
            'temp': str(list_of_data['main']['temp']) + 'k',

            'humidity': str(list_of_data['main']['humidity']),
        }
        print(data)
        return render_template('index.html', data=data)
    
    return render_template('index.html', data=None)

if __name__ == '__main__':
    app.run(debug=True)
