import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "992dc94fe5c04e0ea321e5632023b728"
SPOTIFY_CLIENT_SECRET = "20428fa42c194eed93de0dd091447bba"
SPOTIFY_REDIRECT_URI = "https://5000-deangeligiul-prgspotify-s14caz58e17.ws-eu117.gitpod.io/callback" #dopo il login andiamo qui

#config SpotifyOAuth per l'autenticazione e redirect uri
sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private" #permessi x informazioni dell'utente
)

def get_spotify_object(token_info):
    return spotipy.Spotify(auth=token_info['access_token'])