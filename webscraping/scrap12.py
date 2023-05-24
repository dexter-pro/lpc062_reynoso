# Realizado por: Angel Ivan Reynoso Perez :: matricula --> 1748979 :: grupo --> 62
# importamos modulos
import requests
from bs4 import BeautifulSoup

# obtencion de los datos mediante peticion get
url = "https://realpython.github.io/fake-jobs"
page = requests.get(url)

# analizamos contenido con beautifulsoup
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id='ResultsContainer')

# buscar todos los elementos que el class "card-content"
job_elements = results.find_all("div", class_="card-content")

# busca todos los elementos que el h2 contenga en s texto la palabra python
python_jobs = results.find_all("h2",string=lambda text: "python" in text.lower())

python_jobs_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]

# en objeto job_element buscamos solo python jobs
for job_element in python_jobs_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    # buscamos elementos con la etiqueta "a"
    link_url = job_element.find_all("a")[1]["href"]
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    
    # mostramos salida con link_url
    print(f'Apply here: {link_url}\n')
    print()