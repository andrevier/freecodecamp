# Example of how to parse json data format.
# from python for everybody at freecodecamp.org
# 12/06/22
import json

data ='''{
      "name" : "Chuck",
      "phone" : {
        "type" : "int1",
        "number" : "+1 734 303 4456"
      },
      "email" : {
        "hide" : "yes"
      }
    }'''
info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info['email']['hide'])