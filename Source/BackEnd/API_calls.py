import requests

class PrayerTimesAPI():
    def __init__(self, city, country, method=2):
        self.city = city
        self.country = country
        self.method = method

    def run(self):
        url = f" http://api.aladhan.com/v1/timingsByCity?city={self.city}&country={self.country}&method={self.method}"

        try:
            response = requests.get(url)
            info = response.json()
            if "data" in info:
                times = info['data']["timings"]
                return times
        except Exception as e:
            return f"an unexpected error occurred {e}"
