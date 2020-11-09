import sys
import spotipy
import spotipy.util as util
import datetime

# 0.Spotifyと接続
username = "sm75tpoxa0ur9uf8sduo95ktb"
# リダイレクトURIは深く考えずにこれでOK。詳細はググる。
token = util.prompt_for_user_token(username, client_id='ddac8c0ffa484b3197389904ceb16522',client_secret='95b19559cbb24d7691f77d37f776339a',redirect_uri='http://example.com')

# 1.「☆now」のプレイリストのIDを特定する
sp = spotipy.Spotify(auth=token)
playlists = sp.current_user_playlists()

now_playlist_name = sys.argv[1]
for i, item in enumerate(playlists['items']):
    if item['name'] == now_playlist_name:
        playlist_id = item['id']
# 2.「☆now」を「☆now_日付」リネームする
d_today = str(datetime.date.today())
name = now_playlist_name + d_today

scope = 'playlist-modify-public playlist-modify-private'
token = util.prompt_for_user_token(username,scope, client_id='ddac8c0ffa484b3197389904ceb16522',client_secret='95b19559cbb24d7691f77d37f776339a',redirect_uri='http://example.com')

sp = spotipy.Spotify(auth=token)

sp.user_playlist_change_details(username, playlist_id, name=name)

# 3.「☆now」の名前で新規プレイリストを作成する
playlist_name = now_playlist_name
description = 'new_now'

playlist_create = sp.user_playlist_create(username, playlist_name,public=True, description=description)

# 4.「☆now_日付」に入っている曲を抽出し、同じ曲を「☆now」に追加する
offset = 0
while True:
    playlist_now  = sp.user_playlist_tracks(username,playlist_id=playlist_id, offset=offset)
    for i, item in enumerate(playlist_now['items']):
        results = sp.user_playlist_add_tracks(username, playlist_create['id'], [item['track']['id']])
    if i < 99:
        break
    else:
        offset += 100
