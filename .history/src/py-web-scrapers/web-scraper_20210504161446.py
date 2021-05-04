  
import urllib2
import csv
from datetime import datetime
from bs4 import BeautifulSoup

#webpage to scrape
recipes = 'https://www.allrecipes.com/'

#actual html of page
page = urllib2.urlopen(recipes)

#page parsed for bs4
soup = BeautifulSoup(page, 'html.parser')

recipe_containers = soup.find_all('h2', attrs={'class': 'recipe-nutrition-section'} )
# Output to csv file
for recipe_container in recipe_containers:
    facts = recipe_containers.text
    if 'calories' in facts:
        with open('index.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([facts])