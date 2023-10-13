from bs4 import BeautifulSoup
import requests

url = 'https://www.allrecipes.com/recipe/268494/basic-air-fryer-hot-dogs/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.text, 'html.parser')

# recipe = content.findAll('li', attrs={"class": "mntl-structured-ingredients__list-item"}).text

for recipe in content.findAll('li', attrs={"class": "mntl-structured-ingredients__list-item"}):print (recipe.text.encode('utf-8'))

# print(recipe)
