import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "2d08b992e87f41b6a5d8b5aa30817b6c"
SPOTIFY_CLIENT_SECRET = "a6dab17dd60b49b8b4629f518310894c"
SPOTIFY_REDIRECT_URI = "https://5000-deangeligiulia-spotify1-rn3aand8dks.ws-eu117.gitpod.io/callback" #dopo il login andiamo qui

#config SpotifyOAuth per l'autenticazione e redirect uri
sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private" #permessi x informazioni dell'utente
)

def get_spotify_object(token_info):
    return spotipy.Spotify(auth=token_info['access_token'])