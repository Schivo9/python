import requests
from lxml import html

response = requests.get('https://dolarhoje.com')

site = html.fromstring(response.content)

print(str(site.xpath('//*[@id="nacional"]')[0].value))
