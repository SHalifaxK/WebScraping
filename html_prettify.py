from bs4 import BeautifulSoup
import requests

reps = requests.get('http://ilmatieteenlaitos.fi/saa/sodankyl%C3%A4')
soup = BeautifulSoup(reps.text)
so = soup.prettify()
with open('soup.txt', 'a') as f:
    for line in so:
        f.write(line.encode('utf-8'))
