# Nombre: Angel Ivan Reynoso Perez
# Matricula: 1748979

#importanto fernet desde cryptography
from cryptography.fernet import Fernet

#definicion de funcion genwrite que genera una llave para cifrado
def genwrite():
    key = Fernet.generate_key()
    with open('pass.key', 'wb') as key_file:
        key_file.write(key)
        
#Llamamos la funcion para generar el archivo pass.key
genwrite()

# definimos funcion call_key con la cual leemos el contenido del archivo pass.key
def call_key():
    return open('pass.key', 'rb').read()

# ahora ciframos un mensaje almacenado y codificado previamente
key = call_key()
banner = "LSTI es la mejor carrera".encode()
a = Fernet(key)
coded_banner = a.encrypt(banner)
print(coded_banner)

# desciframos el mensaje previamente cifrado
key = call_key()
b = Fernet(key)
decoded_banner = b.decrypt(coded_banner)
print(decoded_banner)