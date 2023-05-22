Clear-Host
Write-Host "Bienvenido a un ejemplo de codificacion / decodificacion base 64 usando powershell" -ForegroundColor Green
Write-Host "codificando un archivo de texto"

# se va a leer el contenido del archivo de texto
$inputfile = "C:\Users\dexter\Desktop\fcfm\3ro\laboratorio_ciberprog\ev_7\secret.txt"
$fc = Get-Content $inputfile
$GB = [System.Text.Encoding]::UTF8.GetBytes($fc)
$etext = [System.Convert]::ToBase64String($GB)
Write-Host "El contenido del archivo CODIFICADO es: " $etext -ForegroundColor Green

# decodificando contenido de un archivo
Write-Host "Decodificando el texto previo: "
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($etext)) | Out-File -Encoding "ASCII" "C:\Users\dexter\Desktop\fcfm\3ro\laboratorio_ciberprog\ev_7\decoded_secret.txt"
$outfile12 = Get-Content "C:\Users\dexter\Desktop\fcfm\3ro\laboratorio_ciberprog\ev_7\decoded_secret.txt"
Write-Host "El texto decodificado es el siguiente: "
Write-Host "Decodificado: " $outfile12