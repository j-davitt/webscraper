from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.text, 'html.parser')

print(content)
