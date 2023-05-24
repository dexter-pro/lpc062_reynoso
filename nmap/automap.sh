#!/bin/bash
# Realizado por Angel Ivan Reynoso Perez :: 1748979 :: Grupo 062

function net_scan(){
    read -p "Ingrese la subred a escanear: " subred
    echo "Iniciando Scan en $subred..."
    nmap -sn "$subred/24" > escaneo1.txt
}

function indiv_scan(){
    read -p "Ingrese la Ip individual a escanear: " ip
    echo "Iniciando Scan en $ip..."
    nmap --script ssl-poodle $ip > escaneo2.txt
    echo "El archivo se encuentra en $(pwd)/escaneo2.txt"
}

function udp_scan() {
    read -p "Ingrese la Ip a escanear (UDP): " ip
    echo "Iniciando UDP Scan en $ip..."
    sudo nmap -sU -v $ip > escaneo3.txt
    echo "El archivo se encuentra en $(pwd)/escaneo3.txt"
}

function script_scan(){
    read -p "Ingrese el script a ejecutar" scp
    read -p "Ingrese la Ip a escanear: " ip
    echo "Iniciando Script Scan en $ip..."
    sudo nmap --script $scp $ip > escaneo4.txt
    echo "El archivo se encuentra en $(pwd)/escaneo4.txt"
}

echo "|"
echo "|---------------------------|"
echo "|   Menu Principal          |"
echo "|---------------------------|"
echo "|1. Escaneo de Red"
echo "|2. Escaneo Individual"
echo "|3. Escaneo UDP"
echo "|4. Escaneo de Script"
echo "|5. Salir"
echo "|"
read -p "Opción  [ 1 - 5 ] " c
case $c in
    1) net_scan;;
    2) indiv_scan;;
    3) udp_scan;;
    4) script_scan;;
    5) echo "Bye!"; exit 0;;
esac