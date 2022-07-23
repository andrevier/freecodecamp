# Exercise of databases from freecodecamp.org
# The code reads a .txt file and counts the emails after the 'FROM:'.
# source: 15 - Database Email - Python for Everybody Course. 
# https://www.youtube.com/watch?v=uQ3Qv1z_Vao
# date 16/06/22

import sqlite3

# Two steps to connect with the database. There is no previous db file.
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute(''' 
CREATE TABLE Counts (email Text, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1):
  fname = 'mbox-short.txt'

fh = open(fname)

for line in fh:
  # continue if it's the email section.
  if not line.startswith('From: '): continue
  
  pieces = line.split()
  email = pieces[1]
  cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
  row = cur.fetchone()
  
  if row is None:
    cur.execute('''INSERT INTO Counts (email, count)
                   VALUES (?, 1)''', (email,))
  else:
    cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                (email,))
  conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'  

for row in cur.execute(sqlstr):
  print(str(row[0]), row[1])

cur.close()

