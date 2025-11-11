import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv() #loads/gets credentials from file

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
#authentication

scope = (
    "user-library-read "
    "user-library-modify "
    "playlist-read-private "
    "playlist-modify-private "
    "playlist-modify-public "
    "user-top-read user-read-recently-played"
)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
))

#  Fetch your playlists
playlists = sp.current_user_playlists()
for idx, playlist in enumerate(playlists['items']):
    print(f"{idx + 1}: {playlist['name']} (ID: {playlist['id']})")