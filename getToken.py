import base64, json, requests

def get_token(client_id, client_secret):
    tokenurl = 'https://accounts.spotify.com/api/token'

    payload = 'grant_type=client_credentials'

    ori_auth = client_id + ':' + client_secret
    authorization = 'Basic ' + str(base64.b64encode(ori_auth.encode('utf-8')), 'utf-8')

    headers = {
        'Authorization' : authorization, 
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", tokenurl, headers=headers, data = payload)
    if  response.status_code == 200:
        token = response.json()['access_token']
        return token
    else: 
        error_description = response.json()['error_description']
        raise IndexError(error_description)