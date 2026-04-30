import tkinter as tk
def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    result_label.config(text=str(cm) + " cm")
window = tk.Tk()
window.title("Inches to Centimeters")
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="Convert", command=convert)
button.pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()