import requests
from threading import Thread


class PrayerTimesAPI(Thread):
    def __init__(self, city, country, method=2):
        super().__init__()
        self.city = city
        self.country = country
        self.method = method
        self.__times = None

    def run(self):
        return self.fetch()

    def fetch(self):
        url = f" http://api.aladhan.com/v1/timingsByCity?city={self.city}&country={self.country}&method={self.method}"

        try:
            response = requests.get(url)
            info = response.json()
            if "data" in info:
                self.__times = info['data']["timings"]
                return self.__times
        except Exception as e:
            print(e)
            return None

    def get_times(self):
        return self.__times
