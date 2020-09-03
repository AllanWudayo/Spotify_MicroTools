import jsonpath, requests

def seturl(playlistid):
    url = 'https://api.spotify.com/v1/playlists/' + playlistid + '/tracks'
    return url


def getsecplaylist(token, offset, url):
    headers = {
        'Authorization' : 'Bearer ' + token
    }
    payload = {
        'offset' : offset
    }
    response = requests.request("GET", url, headers=headers, params=payload)

    playlist = jsonpath.jsonpath(response.json(), "$['items'][*]['track']['name']")
    return playlist

def getplaylist(token, playlistid):
    offset = 0
    playlist = []
    url = seturl(playlistid)

    while True:
        secPlaylist = getsecplaylist(token, offset, url)
        if secPlaylist == False:
            return playlist
        else:
            playlist.extend(secPlaylist)
            offset += 100