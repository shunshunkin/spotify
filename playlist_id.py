import spotipy
import sys
import pprint
from spotify_token import Spotify_token

username = "sm75tpoxa0ur9uf8sduo95ktb"

ST = Spotify_token(username)
token = ST.set()

sp = spotipy.Spotify(auth=token)
playlists = sp.current_user_playlists()

now_playlist_name = "all"
for i, item in enumerate(playlists['items']):
    if item['name'] == now_playlist_name:
        playlist_id = item['id']
    print(item['name'])
    print(item['id'])
    print('')
