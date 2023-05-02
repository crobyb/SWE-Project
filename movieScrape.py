import requests
import json
from bs4 import BeautifulSoup

url = "https://www.fandango.com/movies-in-theaters"
r = requests.get(url)

#Creating a BeautifulSoup object and passing the content of the site and the parser library
soup = BeautifulSoup(r.content, 'lxml')

#Collecting all of the postercards available
movieCards = soup.find_all('li', class_ = 'poster-card poster-card__fluid browse-movielist--item')

dict = []

#For each card in the movieCards collected,
for card in movieCards:
    #collect all the information for each movie,
    movieTitle = card.find('span', class_ = 'heading-style-1 browse-movielist--title poster-card--title').text

    #add the information to a dictionary
    case = {
        "title": movieTitle,
        "date": "",
        "time": "",
        "description": "",
        "theater": "",
        "location": ""
    }
    
    #then append each dictionary to the list
    dict.append(case)

#Convert the python dict in to a json string then write the json string to a json file
jsonString = json.dumps(dict, indent = 4, default = str)

with open("movies.json", "w") as f:
    f.write(jsonString)