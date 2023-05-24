# Realizado por Angel Reynoso - 1748979 :: Grupo 062

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# creamos objeto para enviar correo
conn = smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()

#Cuerpo del mensaje
html = '''
    <html>
        <body>
            <h1>Practica 12</h1>
            <p>Ejercicio de la practica 12 para envio de correos</p>
            <p>Alumno: Angel Reynoso </p>
            <p>Matricula: 1748979 </p>
            
            <img src="fcfm_cool.png" alt="Logo FCFM Cool"> 
        </body>
    </html>
    '''
    
email_message = MIMEMultipart()
email_message['Subject'] = 'Prueba de envio (script Python) - 1748979'

#Adjuntamos el html
email_message.attach(MIMEText(html, "html"))

# Convertimos en string
email_string = email_message.as_string()

#iniciamos ttls
conn.starttls()

# pedimos credenciales
corr=input('Correo remitente: ')
conn.login(corr, input('Contraseña: '))

# envia correo
conn.sendmail(corr, 'gerardo.bernal@uanl.edu.mx', email_string)

# cerramos conexion
conn.quit()

print('Mensaje enviado!')
