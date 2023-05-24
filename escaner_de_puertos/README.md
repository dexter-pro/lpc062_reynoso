## Práctica 11: Escaneo de puertos

En [scan port v1](./scan_portv1.py) se escanean un rango de puertos de un determinado host, y se almacenan en una lista los puertos abiertos.

En [scan port v2](./scan_portv2.py) se utiliza la librería sockets para probar una lista de puertos sobre las IPs almacenadas

En [scan port v3](./scan_portv3.py) se verifica con socket si algún puerto de parámetro se encuentra abierto

En [scan practica](./script_practica.py) se utilizan algunas partes de los scripts anteriores para crear un menú, y el usuario selecciona el tipo de escaneo que desea ejecutar.