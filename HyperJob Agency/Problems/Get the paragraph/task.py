import requests

from bs4 import BeautifulSoup

word, link = input(), input()

r = requests.get(link)
soup = BeautifulSoup(r.content, 'html.parser')

for par in soup.find_all("p"):
    if word in par.text:
        print(par.text)
        break
