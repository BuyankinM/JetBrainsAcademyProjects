import requests

from bs4 import BeautifulSoup

num_act = int(input())
r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.find_all("a")[num_act - 1].get("href"))