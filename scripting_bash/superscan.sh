#!/bin/bash
# Script superscan.sh
# Marzo 06, 2023 - Angel Ivan Reynoso Perez
#
# Ejemplo de Menu en BASH
date
echo "|"
echo "|---------------------------|"
echo "|   Menu Principal          |"
echo "|---------------------------|"
echo "|1. Net Discover"
echo "|2. Port Scan"
echo "|3. Welcome"
echo "|4. Exit"
echo "|"
read -p "Opción  [ 1 - 4 ] " c
case $c in
    1) ./netdiscover.sh;;
    2) ./portscanv1.sh 192.168.100.89;;
    3) ./welcome.sh;;
    4) echo "Bye!"; exit 0;;
esac