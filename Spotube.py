from tkinter import *

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

window = Tk()
window.geometry("600x600")
window.title("Spotube")
window.configure(background="#000000")
center_window(window, 600, 600)

icon = PhotoImage(file='C:\Visual Studio Code\Project\Python\Spotube\icon.png')
window.iconphoto(True, icon)

text = Text(window, height=1, font=("Comic Sans MS", 20), bg="#000000", bd=0, relief="flat")

text.tag_configure("part1", foreground="#1ED760")
text.insert("end", "---------------------- Spo", "part1")

text.tag_configure("part2", foreground="#FF0000")
text.insert("end", "tube ----------------------", "part2")

buttonExit = Button(window, text="Exit", font=("Comic Sans MS", 20), bg="#FFFFFF", fg="#000000", width=10, height=1, command=window.destroy)
buttonExit.place(relx=0.5, rely=0.83, anchor=CENTER)

text.pack(pady=60)

window.mainloop()