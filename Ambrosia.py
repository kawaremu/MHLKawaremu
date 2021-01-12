import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
import json


client_id = 'df4779725c4946fe95f8b25e5e8f5750'
client_secret = 'dce34e9b65394455a2ba32da7d3521d6'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

name = input('Enter the artist name :')
result = sp.search(name) #search query
list_tracks = result['tracks']['items']
artist_id = str(list_tracks[0])
	

artist_uri = 'spotify:artist:'+artist_id

results_albums = sp.artist_albums(artist_uri, album_type='album')
albums = results_albums['items']
while results_albums['next']:
    results_albums = sp.next(results_albums)
    albums.extend(results_albums['items'])

for album in albums:
    print(album['name'])