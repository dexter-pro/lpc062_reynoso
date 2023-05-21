#Realizado por: Angel Ivan Reynoso Perez :: 1748979 :: Grupo 062
#escaneo de equipos activos en la subred

#determinando gateway

$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "Tu gateway es: " $subred

# determinando rango de subred
$rango = $subred.Substring(0, $subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 3)
Write-Host $rango

#Determinando si rango termina en .

$punto = $rango.EndsWith('.')
if ($punto -like "False"){
    $rango = $rango + '.'
}

# Creamos un array con 254 numeros y se almacenan en una variable
#llamada $rango_ip

$rango_ip = @(1..254)

#Generamos bucle foreach para validad hosts activos en nuestra subred

foreach ($r in $rango_ip){
    $actual = $rango + $r # se genera direccion ip
    $responde = Test-Connection $actual -Quiet -Count 1
    if ($responde -eq "True"){
        Write-Output ""
        Write-Host "Host responde: " -NoNewline; Write-Host $actual -ForegroundColor Green
    }
}

# fin script