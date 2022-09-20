import requests
from bs4 import BeautifulSoup

r = requests.get('https://movil.titsa.com/infoparada.php?IdParada=4132')

soup = BeautifulSoup(r.text, 'html.parser')

tag = soup.h3
type(tag)
print(soup.title.string)