from bs4 import BeautifulSoup
import string

import requests

site = requests.get("https://www.climatempo.com.br/").content
#objeto site recebendo o conteudo da requisicao do site...
soup = BeautifulSoup(site, 'html.parser')
#objeto soup baixando do site o html
#print(soup.prettify())
#transforma html em string e o print vai exibir o html

#temperatura = soup.find("a", class_="link actTriggerGA")

#print(temperatura.string)

print(soup.find('senha'))