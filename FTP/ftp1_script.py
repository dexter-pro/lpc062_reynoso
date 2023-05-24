# Realizado por: Angel Ivan Reynoso Perez :: matricula --> 1748979 :: grupo --> 62

#Conexion y transferencia a Ftp server

# importamos modulo ftp
from ftplib import FTP

# conectamos 
ftp = FTP('192.168.100.125')

# hacemos login
ftp.login('angel','1748979')

# nos ubicamos en la carpeta correcta
ftp.cwd('upload')

# abrimos el archivo y luego lo enviamos
with open('ADVERTENCIA.txt', "rb") as file:
    ftp.storbinary(f"STOR ADVERTENCIA.txt", file)