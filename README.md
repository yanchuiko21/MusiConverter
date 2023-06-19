# MusiConverter
MusiConverter is a small project that allows you to convert a YouTube Music playlist to a Spotify playlist. It utilizes the YouTube API and Spotify API for fetching and creating playlists.

# Prerequisites
To run this project, you need the following:
1. Python 3.x installed on your system.
2. Required Python packages: tkinter, spotipy, and googleapiclient.
3. 

# Installation
1. Clone or download the project files to your local machine.
2. Install the required Python packages by running the following command: pip install spotipy google-api-python-client

# Usage
1. Obtain the required API keys:
- YouTube Data API key: You need to obtain a YouTube Data API key from the Google Developers Console. Make sure to enable the YouTube Data API for your project.
- Spotify client ID and secret: Create a new application on the Spotify Developer Dashboard to get the client ID and secret. Add the redirect URI as http://localhost:8888/callback.

2. Replace the placeholders in the code:
- Replace "YOUR_API_KEY" with your YouTube Data API key in the get_youtube_playlist() function.
- Replace "YOUR_CLIENT_ID" and "YOUR_SECRET_ID" with your Spotify client ID and secret in the create_spotify_playlist() and convert_playlist() functions.

3. Run the main.py file: python main.py
- The MusiConverter GUI window will appear.
- Enter the YouTube Music playlist ID and your Spotify user ID in the respective input fields.
- Click the "Submit" button to start the conversion process.
- If the playlist conversion is successful, you will see a success message. Otherwise, an error message will be displayed.
- You can exit the application by clicking the "Exit" button.

Note: Make sure your system has an active internet connection for the APIs to work properly.

# Icon
An icon image has been added to the MusiConverter GUI window. You can customize the icon by replacing the placeholder <path_to_icon_file> with the actual file path of your icon image in the main.py file.

# Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

# License
This project is licensed under the MIT License.