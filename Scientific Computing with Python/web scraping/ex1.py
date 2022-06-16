# Example of the module 
# from https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# 13/06/22
from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())

print(f"the title tag has: {soup.title}\n")
print(f"the title name: {soup.title.string}\n")
print(f"the p tag has: {soup.p}\n")
print(f"the p tag string:\n{soup.p.string}\n")
print(f"the 1st 'a' tag has:\n{soup.a}\n")
print(f"all the 'a' tags:\n{soup.find_all('a')}\n")
print(f"id specific query:\n{soup.find(id = 'link3')}\n")

# Extracting all the urls of a page's 'a' tags
print('all the urls from the a tag:a\n')
for link in soup.find_all('a'):
    print(link.get('href')) 

# Extracting all the text from the page:
print(f'Extracting all the text from the page:\n{soup.get_text()}')