# Database with SQLite examples
import sqlite3

con = sqlite3.connect("example.db")
cur = con.cursor()
cur.execute('''
  CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    name TEXT
  );
''')
name1 = "Melissa Sayuki"
cur.execute(f'''
  INSERT INTO Students (name)
  VALUES (?);
''',(name1,))

cur.execute('''
  SELECT * FROM Students;
''')
print(cur.fetchall())

con.commit()
con.close()
