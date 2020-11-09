# search.py
# shows artist info for a URN or URL

import spotipy
import sys
import pprint
from spotify_token import Spotify_token

# usage
# $ python search.py [ Keyword you want to search ]
username = "sm75tpoxa0ur9uf8sduo95ktb"
search_str = sys.argv[1]

ST = Spotify_token(username)
token = ST.set()

sp = spotipy.Spotify(auth=token)
result = sp.search(search_str, limit=50)
for item in result['tracks']['items']:
    print(item['name'])
    print(item['id'])
    print('')
