import tkinter as tk
from datetime import date
def calculate_age():
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())
    today = date.today()
    age = today.year - year
    if (today.month, today.day) < (month, day):
        age -= 1
    result_label.config(text="Present Age = " + str(age))
window = tk.Tk()
window.title("Age Calculator")
tk.Label(window, text="Day").pack()
day_entry = tk.Entry(window)
day_entry.pack()
tk.Label(window, text="Month").pack()
month_entry = tk.Entry(window)
month_entry.pack()
tk.Label(window, text="Year").pack()
year_entry = tk.Entry(window)
year_entry.pack()
tk.Button(window, text="Calculate Age", command=calculate_age).pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()