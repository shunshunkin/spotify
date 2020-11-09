# add_tracks_to_playlist.py

import pprint
import sys

import spotipy
import spotipy.util as util
from spotify_token import Spotify_token

username = "sm75tpoxa0ur9uf8sduo95ktb"
playlist_id = sys.argv[1]
track_ids = sys.argv[2:]

ST = Spotify_token(username)
token = ST.set()

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print(results)
else:
    print("Can't get token for", username)
