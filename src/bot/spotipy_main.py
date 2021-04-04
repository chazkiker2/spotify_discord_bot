import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

scope = "user-library-read"
auth_manager = None
sp = None


def fire_spotify_login():
    global auth_manager
    global sp

    auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=scope
    )

    sp = spotipy.Spotify(auth_manager=auth_manager)
    

def test_results():
    global sp

    if sp is not None:
        results = sp.current_user_saved_tracks()
        return_str = ""
        for idx, item in enumerate(results['items']):
            track = item['track']
            return_str += f"\n***\t{idx} {track['artists'][0]['name']} – {track['name']})"

        return return_str
    else:
        return "ERROR"
