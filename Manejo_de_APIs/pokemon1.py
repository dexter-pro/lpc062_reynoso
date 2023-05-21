import requests

# nombre: Angel Ivan Reynoso Perez
# matricula: 1748979

if __name__ =='__main__':
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', [])

        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)
