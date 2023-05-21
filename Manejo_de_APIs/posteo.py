import requests
import json

if __name__ == '__main__':
    url = "http://httpbin.org/post"
    args = {'nombre': 'angel',
            'matricula':'1748979',
            'curso':'Programacion para ciberseguridad'}

    response = requests.post(url, params=args)

    if response.status_code == 200:
        print(response.content)