import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://realpython.github.io/fake-jobs/"

print("Descargando la página web...")
response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    job_elements = soup.find_all("div", class_="card-content")
    
    lista_empleos = []
    
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        
        link_element = job_element.find_parent("div", class_="card").find_all("a")[1]
        link_url = link_element["href"]
        
        lista_empleos.append({
            "Puesto": title_element.text.strip(),
            "Empresa": company_element.text.strip(),
            "Ubicacion": location_element.text.strip(),
            "Enlace": link_url
        })
    
    df = pd.DataFrame(lista_empleos)
    df.to_csv("ofertas_empleo.csv", index=False, encoding="utf-8")
    print("¡Archivo 'ofertas_empleo.csv' actualizado con enlaces!")
else:
    print("Error al descargar la página.")