import tkinter as tk
from tkinter import ttk,messagebox

methods = ["Shia Ithna-Ansari", "University of Islamic Sciences, Karachi", "Islamic Society of North America",
          "Muslim World League", "Umm Al-Qura University, Makkah", "Egyptian General Authority of Survey",
          "Institute of Geophysics, University of Tehran", "Gulf Region", "Kuwait", "Qatar",
          "Majlis Ugama Islam Singapura, Singapore","Union Organization islamic de France", "Diyanet İşleri Başkanlığı, Turkey",
          "Spiritual Administration of Muslims of Russia","Moonsighting Committee Worldwide", "Dubai"]

if __name__ == '__main__':
    app = tk.Tk()
    app.title("Time Prayer")
    frame = ttk.Frame(app, padding=20)
    frame.grid(row=0, column=0)
    #-----city input -----
    city_label = ttk.Label(frame, text="City:")
    city_label.grid(row=0, column=0, pady=5, padx=5)
    city_entry = ttk.Entry(frame, width=20)
    city_entry.grid(row=0, column=1)
    # -----country input -----
    country_label = ttk.Label(frame, text="Country:")
    country_label.grid(row=1, column=0, pady=5, padx=5)
    country_entry = ttk.Entry(frame, width=20)
    country_entry.grid(row=1, column=1)
    # -----method input -----
    method_label = ttk.Label(frame, text="Method:", state="readonly")
    method_label.grid(row=2, column=0)
    method_combo = ttk.Combobox(frame, width=30)
    method_combo.grid(row=2, column=1, pady=5, padx=5)
    method_combo["values"] = methods
    method_combo.set(methods[3])
    # -----fetching button -----
    fetch_button = ttk.Button(frame, text="Get Prayer Times")
    fetch_button.grid(row=3, column=0, columnspan=2)
    # -----showing results-----
    fajr_label = ttk.Label(frame, text="Fajr: ")
    fajr_label.grid(row=4, column=0)
    sunrise_label = ttk.Label(frame, text="Sunrise: ")
    sunrise_label.grid(row=5, column=0)
    dhuhr_label = ttk.Label(frame, text="Dhuhr: ")
    dhuhr_label.grid(row=6, column=0)
    maghrib_label = ttk.Label(frame, text="Maghrib: ")
    maghrib_label.grid(row=7, column=0)
    isha_label = ttk.Label(frame, text="Isha: ")
    isha_label.grid(row=8, column=0)
    app.mainloop()