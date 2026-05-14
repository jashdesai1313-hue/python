import tkinter as tk
def calculate():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())
    simple_interest = (principal * rate * time) / 100
    compound_interest = principal * ((1 + rate / 100) ** time) - principal
    result_label.config(
        text="Simple Interest = " + str(round(simple_interest, 2)) +
        "\nCompound Interest = " + str(round(compound_interest, 2))
    )
window = tk.Tk()
window.title("Interest Calculator")
tk.Label(window, text="Principal Amount").pack()
principal_entry = tk.Entry(window)
principal_entry.pack()
tk.Label(window, text="Rate of Interest").pack()
rate_entry = tk.Entry(window)
rate_entry.pack()
tk.Label(window, text="Time Period").pack()
time_entry = tk.Entry(window)
time_entry.pack()
tk.Button(window, text="Calculate", command=calculate).pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()