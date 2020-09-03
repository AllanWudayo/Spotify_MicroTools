import requests, json, os, platform, openpyxl
import getToken, getPlaylist

def main():
    client_id = '' #Your client_id
    client_secret = '' #Your client_secret

    try:
        token = getToken.get_token(client_id, client_secret)
    except requests.ConnectionError:
        print('Not Connected!')
    except IndexError as Errmsg:
        print(Errmsg)
    except json.JSONDecodeError:
        print('Configuration Error!')
    else:
        print('Token: ' + token)
        playlistid = input('PlaylistID: ')


        playlist = getPlaylist.getplaylist(token, playlistid)

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = 'playlist'
        

        num = 1
        for name in playlist:
            ws['A'+ str(num)] = name
            print(name)
            num += 1
        try:
            wb.save(os.path.dirname(os.path.abspath(__file__)) + '/playlist.xlsx')
        except Exception:
            print('Err!')

if __name__ == "__main__":
    main()
    pass