import requests

def fetch_prayer_times(city, country, method=2):
    url = f" http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method={method}"

    try:
        response = requests.get(url)
        info = response.json()
        if "data" in info:
            times = info['data']["timings"]
            return times
    except Exception as e:
        return f"an unexpected error occurred {e}"
