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

label = Label(text="---------------------- Spotube ----------------------", font=("Comic Sans MS", 20), bg="#000000", fg="#FFFFFF")
label.place(relx=0.5, rely=0.12, anchor=CENTER)

label = Label(text="Spotify", font=("Comic Sans MS", 20), bg="#000000", fg="#00d204")
label.place(relx=0.5, rely=0.26, anchor=CENTER)

youtube_playlist_id_entry = Entry(window, font=("Comic Sans MS", 20), justify="center")
youtube_playlist_id_entry.place(relx=0.5, rely=0.36, anchor=CENTER)

label = Label(text="YouTube", font=("Comic Sans MS", 20), bg="#000000", fg="#ff0000")
label.place(relx=0.5, rely=0.48, anchor=CENTER)

spotify_user_id_entry = Entry(window, font=("Comic Sans MS", 20), justify="center")
spotify_user_id_entry.place(relx=0.5, rely=0.58, anchor=CENTER)

buttonSubmit = Button(window, text="Sumbit", font=("Comic Sans MS", 18), bg="#FFFFFF", fg="#000000", width=10, height=1)
buttonSubmit.place(relx=0.5, rely=0.78, anchor=CENTER)

buttonExit = Button(window, text="Exit", font=("Comic Sans MS", 18), bg="#FFFFFF", fg="#000000", width=10, height=1, command=window.destroy)
buttonExit.place(relx=0.5, rely=0.90, anchor=CENTER)

window.mainloop()