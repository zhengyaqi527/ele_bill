import requests
import base64

# 获取token

def get_token(client_id=None, client_secret=None):

    grant_type = 'client_credentials'
    if not client_id:
        client_id = 'yQUoOvcQNG2soQGO5UHqCZwe'
    if not client_secret:
        client_secret = 'GeEsc4GEz5oqvpDtLLV7QX4bjB3dzAo1'
    host = 'https://aip.baidubce.com/oauth/2.0/token'

    params = {
        "grant_type": grant_type,
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = (requests.get(host, params=params)).json()
    return response['access_token']
   


def analyse_img(access_token, image_path):
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
    
    f = open(image_path, 'rb')
    img = base64.b64encode(f.read())

    params = {"access_token": access_token}
    data = {"image": img}
    headers = {"content-type": "application/x-www-form-urlencoded"}
    response = requests.post(url, params=params, data=data, headers=headers)
    return response.json()


def ayalyse_bill(img_response):
    words_result = img_response['words_result']





if __name__ == "__main__":
    
    image_path = '/mnt/d/Desktop/ele-2.jpg'
    access_token = get_token()
    res = analyse_img(access_token, image_path)
    print(res)
