import spotipy
from airflow.models import Variable
from spotipy.oauth2 import SpotifyOAuth


def get_spotify_client():
    CLIENT_ID = Variable.get("spotify_client_id")
    CLIENT_SECRET = Variable.get("spotify_client_secret")
    REDIRECT_URI = Variable.get("spotify_redirect_uri")

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope="playlist-modify-private",
        )
    )
    return sp
