from tkinter import *
window = Tk()
window.title("Demo Window")
window.geometry("400x300")
window.config(bg="lightblue")
label = Label(window, text="hello tinker", font = ("Arial", 20))
label.pack(pady = 100)
window.mainloop()