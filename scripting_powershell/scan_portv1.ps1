#Realizado por: Angel Ivan Reynoso Perez :: 1748979 :: Grupo 062

#escaneo de equipos activos en la subred

#determinando gateway

$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "Determinando tu gateway ..."
Write-Host "Tu gateway es: " $subred

# determinando rango de subred
$rango = $subred.Substring(0, $subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 4)
Write-Host "Determinando tu rango de subred ..."
Write-Host $rango

#Determinando si rango termina en .

$punto = $rango.EndsWith('.')
if ($punto -like "False"){
    $rango = $rango + '.'
}

# definimos un array con puertos a escanear
#establecemos una variable para waittime
$portstoscan = @(20,21,22,23,25,50,51,53,80,110,119,135,136,137,138,139,143,161,162,389,442,445,636,1025,1443,3389,5985,5986,8080,10000)
$waittime = 100

# solicitamos direccion ip a escanear
Write-Host "Direccion ip a escanear: " -NoNewline
$direccion = Read-Host

#Generamos bucle foreach para validad hosts activos en nuestra subred
foreach ($p in $portstoscan){
    $TCPObject = New-Object System.Net.Sockets.TcpClient
    try {$resultado = $TCPObject.ConnectAsync($direccion, $p).Wait($waittime)}catch{}
    if ($resultado -eq "True") {
        Write-Host "Puertos abiertos: " -NoNewline; Write-Host $p -ForegroundColor Green
    }
}

# fin script