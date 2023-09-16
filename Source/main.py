import tkinter as tk
import  BackEnd.API_calls as call
from tkinter import ttk,messagebox

methods = ["Shia Ithna-Ansari", "University of Islamic Sciences, Karachi", "Islamic Society of North America",
          "Muslim World League", "Umm Al-Qura University, Makkah", "Egyptian General Authority of Survey",
          "Institute of Geophysics, University of Tehran", "Gulf Region", "Kuwait", "Qatar",
          "Majlis Ugama Islam Singapura, Singapore","Union Organization islamic de France", "Diyanet İşleri Başkanlığı, Turkey",
          "Spiritual Administration of Muslims of Russia","Moonsighting Committee Worldwide", "Dubai"]

prayer_times_labels = []
times_row = 4
default_city = "Cairo"
default_country = "Egypt"
def fetch_times_gui():
    city = city_entry.get()
    country = country_entry.get()
    method = method_combo.current()
    index = 0
    if city and country:
        times = call.fetch_prayer_times(city, country, method)
        del prayer_times_labels[:]
        for name, time in times.items():
            if name != "Sunset" and name != "Imsak" and name != "Midnight" and name != "Firstthird" and name != "Lastthird":
                prayer_times_labels.append(ttk.Label(frame, text=f"{name} : {time}"))
                prayer_times_labels[index].grid(row=times_row + index, column= 0, columnspan=2)
                index = index + 1
    else:
        messagebox.showerror("Error","unable to fetch paryer times, please check your input")


if __name__ == '__main__':
    app = tk.Tk()
    app.title("Time Prayer")
    frame = ttk.Frame(app, padding=20)
    frame.grid(row=0, column=0)
    #-----city input -----
    city_label = ttk.Label(frame, text="City:")
    city_label.grid(row=0, column=0, pady=5, padx=5)
    city_entry = ttk.Entry(frame, width=20)
    city_entry.insert(0, default_city)
    city_entry.grid(row=0, column=1)
    # -----country input -----
    country_label = ttk.Label(frame, text="Country:")
    country_label.grid(row=1, column=0, pady=5, padx=5)
    country_entry = ttk.Entry(frame, width=20)
    country_entry.insert(0, default_country)
    country_entry.grid(row=1, column=1)
    # -----method input -----
    method_label = ttk.Label(frame, text="Method:", state="readonly")
    method_label.grid(row=2, column=0)
    method_combo = ttk.Combobox(frame, width=30)
    method_combo.grid(row=2, column=1, pady=5, padx=5)
    method_combo["values"] = methods
    method_combo.set(methods[3])
    # -----fetching button -----
    fetch_button = ttk.Button(frame, text="Get Prayer Times", command=fetch_times_gui)
    fetch_button.grid(row=3, column=0, columnspan=2)
    fetch_times_gui()
    app.mainloop()