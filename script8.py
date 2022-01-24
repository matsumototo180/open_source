import requests
import datetime

ACCESS_TOKEN = ""

def notify(token, message, imagepath=None, stickerPackageId=None, stickerId=None):
    headers= {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'message': f'{message}',
        'stickerPackageId': stickerPackageId,
        'stickerId': stickerId
    }
    files = {
        'imageFile': None if imagepath is None else open(imagepath, 'rb')
    }
    res = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params, files=files)
    print(res.json())

notify(token=ACCESS_TOKEN, message=f"{datetime.datetime.now():%Y年%m月%d日 %H:%M:%S}", imagepath='./data/pt8/gakusyo.jpg')
notify(token=ACCESS_TOKEN, message="こんにちは", stickerPackageId=789, stickerId=10855)
