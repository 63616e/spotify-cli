import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

def authing(username, auth_manager):
    username = str(username)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    playlist_total_list = sp.user_playlists(username)
    while playlist_total_list:

        playlist_uri_dictioanary = {}
        print("this user has the following playlists as available: ")   
        for i, playlist_uri in enumerate(playlist_total_list['items']):
            
            print(playlist_uri['name'])
            # add playlist name and uri to dictionary
            playlist_uri_dictioanary[playlist_uri['name']
                                     ] = playlist_uri['uri']

        # print("%4d %s %s" %

        #       (i + 1 + playlist_total_list['offset'], playlist_uri['uri'],  playlist_uri['name']))

        if playlist_total_list['next']:

            playlist_total_list = sp.next(playlist_total_list)

        else:

            playlist_total_list = None
    return playlist_uri_dictioanary
