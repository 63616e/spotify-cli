def dictize(playlist_name):

    dicts = {}

    for i in range(len(playlist_name['tracks']['items'])):

        artists = playlist_name['tracks']['items'][i]['track']['artists']

        songs = playlist_name['tracks']['items'][i]['track']['name']

        for i in range(len(artists)):

            dicts[artists[i]['name']] = songs
    return dicts
