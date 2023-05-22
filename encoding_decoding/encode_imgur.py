import requests # para llamar al sitio
import base64 #para encode/decode en base 64
from requests import Response
# Nombre: Angel Ivan Reynoso Perez
# Matricula: 1748979

# Descargar la imagen del sitio
if __name__ == '__main__':
    url = 'https://i.imgur.com/KFT5ZEa.jpeg'
    
    Response: Response = requests.get(url, stream=True)
    with open('space.jpeg', 'wb') as file_down:
        for chunk in Response.iter_content(): #descargando contenido poco a poco
            file_down.write(chunk)
    Response.close()
    
#Para codificar la imagen
with open('space.jpeg', 'rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode(binary_file_data)
    base64_message = base64_encoded_data.decode('utf-8')
    
    print(base64_message)