from bs4 import BeautifulSoup
import urllib2
import re

def getLinks(url):
    html_page = urllib2.urlopen(url)
    soup = BeautifulSoup(html_page)
    links = []

    for link in soup.findAll('a',
                attrs={'href':re.compile("^https://")}):
         links.append(link.get('href'))
    return links

links = getLinks('https://www.kabum.com.br')
print(links)
 
filename = 'teste1.csv'
with open('teste1.csv', 'wb') as f:
    for i in links:
        f.write(i + "\n")
