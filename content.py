import bs4 as bs
import requests
import lxml

#dummy web page for parsing purposes
r = requests.get('https://pythonprogramming.net/parsememcparseface/')
soup = bs.BeautifulSoup(r.content, 'lxml')
print soup
