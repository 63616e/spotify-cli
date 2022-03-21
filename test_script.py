# https://github.com/enjuichang/PracticalDataScience-ENCA


# https://pypi.org/project/spotify-cli/

import spotipy


from spotipy.oauth2 import SpotifyClientCredentials


from spotipy.oauth2 import SpotifyOAuth


from dictionarize import dictize
from authentication import authing

#read cid values from secret.txt where cid is client id and secret is client secret, cid located in the first row, secret in the second row
with open("secret.txt") as f:
    secret_ls = f.readlines()
    cid = secret_ls[0][:-2]
    secret = secret_ls[1]
        

auth_manager = SpotifyClientCredentials(

    cid, secret)

user_name = str(input("Enter your username you want to check: "))
#do the authentication action.
authing(user_name, auth_manager)

# the returned dictionary
playlist_uri_dictioanary = authing(user_name, auth_manager)


client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret)


sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
selected_user_playlist = str(
    input("Enter the name playlist you want to check: "))
for i in range(len(playlist_uri_dictioanary)):

    sample_playlist = sp.user_playlist(

    # pass in the first uri which is the value of the dictionary

    user=None, playlist_id=playlist_uri_dictioanary[selected_user_playlist])

print(dictize(sample_playlist))

