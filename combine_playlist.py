import spotipy
import sys
import pprint
from spotify_token import Spotify_token

username = "sm75tpoxa0ur9uf8sduo95ktb"


offset = 0
while True:
    playlist_now  = sp.user_playlist_tracks(username,playlist_id=playlist_id, offset=offset)
    for i, item in enumerate(playlist_now['items']):
        results = sp.user_playlist_add_tracks(username, playlist_create['id'], [item['track']['id']])
    if i < 99:
        break
    else:
        offset += 100
