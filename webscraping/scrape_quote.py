# Realizado por: Angel Ivan Reynoso Perez :: matricula --> 1748979 :: grupo --> 62

import requests
import csv
from bs4 import BeautifulSoup

# direccion de web
url = "http://quotes.toscrape.com/"

# ejecutar get-request
response = requests.get(url)

# analizar sintacticamente el archivo html de beautifulsoup del texto fuente
html = BeautifulSoup(response.text, 'html.parser')

# extraer todas las citas y autores del archivo html
quotes_html = html.find_all('span', class_="text")
authors_html = html.find_all('small', class_="author")

# crear lista de las citas
quotes = []
for quote in quotes_html:
    quotes.append(quote.text)
    
# crea lista de autores
authors = []
for author in authors_html:
    authors.append(author)

# para hacer test: cmbinar y mostrar las entradas de ambas listas
for t in zip(quotes, authors):
    print(t)
    
with open('./citas_1748979.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes, authors))