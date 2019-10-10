from bs4 import BeautifulSoup
import urllib2
import re


def getLinks(url):
    html_page = urllib2.urlopen(url)
    soup = BeautifulSoup(html_page)
    links = []

    for link in soup.findAll('A',attrs={'href': re.compile("^htt(p|ps)://")}):
        links.append(link.get('href'))

        return links

    links = getLinks("https://www.hltv.org")

