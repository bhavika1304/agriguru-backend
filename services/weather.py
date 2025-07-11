import requests

API_KEY = "56e0aff03e74702188dae2b8096a71e8"  # ✅ Looks valid!

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        # ✅ Check HTTP status
        if response.status_code != 200:
            return {"error": f"API error: {data.get('message', 'Unknown error')}"}

        # ✅ Check presence of 'list' key
        if "list" not in data:
            return {"error": f"Missing 'list' in response: {data}"}

        # ✅ Build forecast output
        forecast = []
        for item in data["list"][:5]:  # First 5 intervals (3-hour each)
            forecast.append({
                "datetime": item["dt_txt"],
                "temp": item["main"]["temp"],
                "humidity": item["main"]["humidity"],
                "rain": item.get("rain", {}).get("3h", 0)
            })

        return {"forecast": forecast}

    except Exception as e:
        return {"error": str(e)}
