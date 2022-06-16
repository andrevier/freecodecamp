# Example of parsing XML file
# from python for everybody at freecodecamp.org
# 12/06/22
import xml.etree.ElementTree as ET

data = '''<person>
  <name>Chuck</name>
  <phone type="int1">
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
