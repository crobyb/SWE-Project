mport requests
import json
from bs4 import BeautifulSoup

url = "https://www.fandango.com/movies-in-theaters"
r = requests.get(url)

#Creating a BeautifulSoup object and passing the content of the site and the parser library
soup = BeautifulSoup(r.content, 'lxml')
print(soup.prettify())

#Collecting all of the postercards available
movieCards = soup.find_all('li', class_ = 'poster-card poster-card__fluid browse-movielist--item')

for cards in movieCards:
    print(cards.text)