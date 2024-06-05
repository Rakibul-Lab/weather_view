from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city_name = request.form["city"]
        api_key = "611e7933054fd0c2b0608d55b7e6616e"  
        weather_data = get_weather(city_name, api_key)

        if weather_data["cod"] == "404":
            error_message = "City not found. Please enter a valid city name."
            return render_template("index.html", error_message=error_message)
        else:
            description = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]

            return render_template("index.html", city=city_name, description=description, temperature=temperature, humidity=humidity, wind_speed=wind_speed)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
