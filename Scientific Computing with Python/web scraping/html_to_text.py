'''Exercise to transform html into text with the proper spaces 
and paragraphs.
Date: 20/09/22'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

def html_to_text(soup):
    '''Receive a tag object from BeautifulSoup and parse the sequence of tags
    into a text, separating the tags in lines.'''
    
    # Rip out all script and style elements and the strong tag.
    for script in soup(["script", "style", "strong"]):
        script.extract() 
    
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())

    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")
for data in soup.findAll('div', {'class', "headlinestory"}):
    headline = html_to_text(data)

for data in soup.findAll('div', {'class', 'bodytext'}):
    bodytext = html_to_text(data)

with open('ex.txt', 'w', encoding='utf-8') as f:
    f.write(headline + '\n')
    f.write(bodytext)
