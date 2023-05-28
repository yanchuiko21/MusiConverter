from tkinter import *
from googleapiclient.discovery import build
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def get_youtube_playlist(youtube_playlist_id):
    youtube = build('youtube', 'v3', developerKey='AIzaSyAx3Y6F7GfEl5MkQQgVddx2l8VOuLMXnGU')
    request = youtube.playlistItems().list(
        part='snippet',
        maxResults=100,
        playlistId=youtube_playlist_id
    )
    response = request.execute()
    return [item['snippet']['title'] for item in response['items']]

def create_spotify_playlist(spotify_user_id, track_uris):
    scope = 'playlist-modify-public'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id="612210be399a424788083d9bcb443bfd", client_secret="abb9b871ac1d4742b04b678285a1834f", redirect_uri="http://localhost:8888/callback"))
    playlist = sp.user_playlist_create(spotify_user_id, "New Playlist from YouTube")
    results = sp.playlist_add_items(playlist['id'], track_uris)

def convert_playlist():
    youtube_playlist_id = youtube_playlist_id_entry.get()
    spotify_user_id = spotify_user_id_entry.get()
    youtube_playlist = get_youtube_playlist(youtube_playlist_id)
    spotify_uris = []
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='playlist-modify-public', client_id="612210be399a424788083d9bcb443bfd", client_secret="abb9b871ac1d4742b04b678285a1834f", redirect_uri="http://localhost:8888/callback"))
    for song in youtube_playlist:
        results = sp.search(q=song, limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            spotify_uris.append(track['uri'])
    create_spotify_playlist(spotify_user_id, spotify_uris)

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

buttonSubmit = Button(window, text="Sumbit", font=("Comic Sans MS", 18), bg="#FFFFFF", fg="#000000", width=10, height=1, command=convert_playlist)
buttonSubmit.place(relx=0.5, rely=0.78, anchor=CENTER)

buttonExit = Button(window, text="Exit", font=("Comic Sans MS", 18), bg="#FFFFFF", fg="#000000", width=10, height=1, command=window.destroy)
buttonExit.place(relx=0.5, rely=0.90, anchor=CENTER)

window.mainloop()