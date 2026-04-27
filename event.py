from tkinter import *
window = Tk()
window. title("Event Handler") 
window.geometry("300x200")
def handle_keypress(event):
    print ("Key Pressed:", event. char)
def handle_click(event):
    print ("Button Clicked!")
window.bind("<Key>", handle_keypress)
button = Button(window, text="Click Me")
button. pack(pady=20)
button. bind("<Button-1>", handle_click)
window.mainloop()
