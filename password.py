import tkinter as tk
def check_password():
    password = entry.get()
    if len(password) < 5:
        result.config(text="Weak Password")
    elif len(password) < 8:
        result.config(text="Medium Password")
    else:
        result.config(text="Strong Password")
window = tk.Tk()
window.title("Password Strength")
label = tk.Label(window, text="Enter Password")
label.pack()
entry = tk.Entry(window, show="*")
entry.pack()
button = tk.Button(window, text="Check", command=check_password)
button.pack()
result = tk.Label(window, text="")
result.pack()
window.mainloop()