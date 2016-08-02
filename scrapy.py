from os.path import basename
from urlparse import urljoin
from lxml import html
import requests
base_url = 'http://www.cde.ca.gov/ds/sp/ai/'
page = requests.get(base_url).text
doc = html.fromstring(page)
hrefs = [a.attrib['href'] for a in doc.cssselect('a')]
xls_hrefs = [href for href in hrefs if 'xls' in href]
for href in xls_hrefs:
  print(href) # e.g. documents/sat02.xls
  url = urljoin(base_url, href)
  with open("/tmp/" + basename(url), 'wb') as f:
    print("Downloading", url)
    # Downloading http://www.cde.ca.gov/ds/sp/ai/documents/sat02.xls
    data = requests.get(url).content
    f.write(data)