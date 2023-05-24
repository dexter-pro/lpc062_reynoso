# Realizado por: Angel Ivan Reynoso Perez :: 1748979 :: Grupo 062
import nmap

def main():
    print('Seleccione una opcion para escanear:')
    print('1) Escaneo UDP')
    print('2) Escaneo Completo')
    print('3) Deteccion de sistema operativo')
    print('4) Escaneo de red con ping')

    opc = int(input())
    escaner = nmap.PortScanner()
     
    if opc == 1:
        print(escaner.scan('192.168.100.89', '1-1024', '-v -sU'))
    elif opc == 2:
        escaner.scan('192.168.100.89', '1-1024', '-v -sU -o -p 22-80')
    elif opc == 3:
        escaner.scan('192.168.100.89', '1-1024', '-v -sV -o')
    elif opc == 4:
        escaner.scan('192.168.100.89', '1-1024', '-v -sP')



if __name__ == '__main__':
    main()