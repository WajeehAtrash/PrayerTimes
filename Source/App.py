import tkinter as tk
import BackEnd.API_calls as Call
from tkinter import ttk, messagebox
from threading import Lock

DONT_SHOW_MESSAGE = 0
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Time Prayer")
        self.__private_default_city = "Cairo"
        self.__private_default_country = "Egypt"
        self.__private_prayer_times_labels = []
        self.__private_methods = ["Shia Ithna-Ansari", "University of Islamic Sciences, Karachi",
                                  "Islamic Society of North America", "Muslim World League",
                                  "Umm Al-Qura University, Makkah", "Egyptian General Authority of Survey",
                                  "Institute of Geophysics, University of Tehran", "Gulf Region", "Kuwait", "Qatar",
                                  "Majlis Ugama Islam Singapura, Singapore", "Union Organization islamic de France",
                                  "Diyanet İşleri Başkanlığı, Tukey", "Spiritual Administration of Muslims of Russia",
                                  "Moonsighting Committee Worldwide", "Dubai"]
        self.__private_times_row = 4
        self.__create_body_frame()
        self.__request_lock = Lock()

    def __create_body_frame(self):
        self.body = ttk.Frame(self)

        #-----city input -----
        self.city_label = ttk.Label(self.body, text="City:")
        self.city_label.grid(row=0, column=0, pady=5, padx=5)
        self.city_entry = ttk.Entry(self.body, width=20)
        self.city_entry.insert(0, self.__private_default_city)
        self.city_entry.grid(row=0, column=1)

        # -----country input -----
        self.country_label = ttk.Label(self.body, text="Country:")
        self.country_label.grid(row=1, column=0, pady=5, padx=5)
        self.country_entry = ttk.Entry(self.body, width=20)
        self.country_entry.insert(0, self.__private_default_country)
        self.country_entry.grid(row=1, column=1)

        # -----method input -----
        self.method_label = ttk.Label(self.body, text="Method:", state="readonly")
        self.method_label.grid(row=2, column=0)
        self.method_combo = ttk.Combobox(self.body, width=30)
        self.method_combo.grid(row=2, column=1, pady=5, padx=5)
        self.method_combo["values"] = self.__private_methods
        self.method_combo.set(self.__private_methods[3])

        # -----fetching button -----
        self.fetch_button = ttk.Button(self.body, text="Get Prayer Times")
        self.fetch_button['command'] = self.__fetch_times
        self.fetch_button.grid(row=3, column=0, columnspan=2)

        # attach the body frame
        self.body.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)
        self.__fetch_times_start()

    def __fetch_times_start(self):
        city = self.city_entry.get()
        country = self.country_entry.get()
        method = self.method_combo.current()
        if city and country:
            api_call = Call.PrayerTimesAPI(city, country, method)
            times = api_call.fetch()
            self.__show_times(times, DONT_SHOW_MESSAGE)
        else:
            messagebox.showerror("Error", "Please enter a country and city names")

    def __fetch_times(self):
        self.fetch_button['state'] = tk.DISABLED
        with self.__request_lock:
            city = self.city_entry.get()
            country = self.country_entry.get()
            method = self.method_combo.current()
            if city and country:
                api_call = Call.PrayerTimesAPI(city, country, method)
                api_call.start()
                self.monitor(api_call)
            else:
                messagebox.showerror("Error", "Please enter a country and city names")

    def monitor(self, thread):

        if thread.is_alive():
            # check the thread every 100ms
            self.after(100, lambda: self.monitor(thread))
        else:
            times = thread.get_times()
            self.__show_times(times)
            self.fetch_button['state'] = tk.NORMAL

    def __show_times(self, times, show_message=1):
        index = 0
        del self.__private_prayer_times_labels[:]
        if times is not None:
            for name, time in times.items():
                if name != "Sunset" and name != "Imsak" and name != "Midnight" and name != "Firstthird" \
                        and name != "Lastthird":
                    self.__private_prayer_times_labels.append(ttk.Label(self.body, text=f"{name} : {time}"))
                    self.__private_prayer_times_labels[index].grid(row=self.__private_times_row + index, column=0,
                                                                   columnspan=2)
                    index = index + 1
            if show_message:
                messagebox.showinfo("Success", "Times fetched successfully")
        else:
            messagebox.showerror("Error", "unable to fetch prayer times, please check your input")


if __name__ == "__main__":
    app = App()
    app.mainloop()
