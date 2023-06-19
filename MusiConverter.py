from tkinter import *  # GUI
from tkinter import messagebox # Error messages
import spotipy  # Spotify API
from googleapiclient.discovery import build  # YouTube API
from spotipy.oauth2 import SpotifyOAuth  # Authenticating requests

# Centering the GUI window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Getting the YouTube Music Playlist
def get_youtube_playlist(youtube_playlist_id):
    youtube = build('youtube', 'v3', developerKey='YOUR_API_KEY')
    all_items = []
    try:
        request = youtube.playlistItems().list(
            part='snippet',
            maxResults=50,
            playlistId=youtube_playlist_id
        )
        while request is not None:
            response = request.execute()
            for item in response['items']:
                video_id = item['snippet']['resourceId']['videoId']
                video_request = youtube.videos().list(
                    part='snippet',
                    id=video_id
                )
                video_response = video_request.execute()
                if video_response['items']:
                    video_info = video_response['items'][0]['snippet']
                    title = video_info['title']
                    artist = video_info['channelTitle']
                    all_items.append((title, artist))
            request = youtube.playlistItems().list_next(request, response)
    except Exception as e:
        messagebox.showerror("Error", "Invalid YouTube Music Playlist ID. Please check the ID and try again.")
        raise Exception("Invalid YouTube Music Playlist ID")
    return all_items

# Creating the Spotify Playlist
def create_spotify_playlist(spotify_user_id, track_uris):
    scope = 'playlist-modify-public'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id="YOUR_CLIENT_ID", client_secret="YOUR_SECRET_ID", redirect_uri="http://localhost:8888/callback"))
    playlist = sp.user_playlist_create(spotify_user_id, "Playlist")
    chunks = [track_uris[i:i + 100] for i in range(0, len(track_uris), 100)]
    for chunk in chunks:
        results = sp.playlist_add_items(playlist['id'], chunk)

# Converting the YouTube Music Playlist to a Spotify Playlist
def convert_playlist():
    try:
        youtube_playlist_id = youtube_playlist_id_entry.get()
        spotify_user_id = spotify_user_id_entry.get()
        if not youtube_playlist_id:
            messagebox.showerror("Error", "YouTube Music Playlist ID is empty. Please check the ID and try again.")
            return
        if not spotify_user_id:
            messagebox.showerror("Error", "Spotify User ID is empty. Please check the ID and try again.")
            return
        try:
            youtube_playlist = get_youtube_playlist(youtube_playlist_id)
        except Exception as e:
            return
        spotify_uris = []
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='playlist-modify-public', client_id="YOUR_CLIENT_ID", client_secret="YOUR_SECRET_ID", redirect_uri="http://localhost:8888/callback"))
        for song, artist in youtube_playlist:
            artist = artist.replace(" - Topic", "")
            query = f"track:{song} artist:{artist}"
            results = sp.search(q=query, limit=1)
            if results['tracks']['items']:
                track = results['tracks']['items'][0]
                spotify_uris.append(track['uri'])
        try:
            create_spotify_playlist(spotify_user_id, spotify_uris)
        except Exception:
            messagebox.showerror("Error", "Invalid Spotify User ID. Please check the ID and try again.")
            return
        messagebox.showinfo("Successful", "The YouTube Music Playlist has been converted to a Spotify Playlist.")
    except Exception as e:
        messagebox.showerror("Error", "Unknown Error")

# GUI
window = Tk()
window.geometry("600x600")
window.title("MusiConverter")
window.configure(background="#A4DBC0")
center_window(window, 600, 600)

icon = PhotoImage(file='C:\Visual Studio Code\Project\Python\MusiConverter\icon.png')
window.iconphoto(True, icon)

label = Label(text="---------------------- MusiConverter ----------------------", font=("Comic Sans MS", 20), bg="#A4DBC0", fg="#000000")
label.place(relx=0.5, rely=0.12, anchor=CENTER)

label = Label(text="YouTube Music", font=("Comic Sans MS", 20), bg="#A4DBC0", fg="#FF0000")
label.place(relx=0.5, rely=0.28, anchor=CENTER)

youtube_playlist_id_entry = Entry(window, font=("Comic Sans MS", 20), bg="#F0FCFF", justify="center")
youtube_playlist_id_entry.place(relx=0.5, rely=0.38, anchor=CENTER)

label = Label(text="Spotify", font=("Comic Sans MS", 20), bg="#A4DBC0", fg="#159442")
label.place(relx=0.5, rely=0.50, anchor=CENTER)

spotify_user_id_entry = Entry(window, font=("Comic Sans MS", 20), bg="#F0FCFF", justify="center")
spotify_user_id_entry.place(relx=0.5, rely=0.60, anchor=CENTER)

buttonSubmit = Button(window, text="Sumbit", font=("Comic Sans MS", 18), bg="#FFFFFF", fg="#000000", width=10, height=1, command=convert_playlist)
buttonSubmit.place(relx=0.5, rely=0.81, anchor=CENTER)

buttonExit = Button(window, text="Exit", font=("Comic Sans MS", 18), bg="#FFFFFF", fg="#000000", width=10, height=1, command=window.destroy)
buttonExit.place(relx=0.5, rely=0.92, anchor=CENTER)

window.mainloop()