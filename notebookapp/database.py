# Database classes and management.
import sqlite3

class UserDB:
  '''Implement a database for the users' Id and passwords.'''
  def __init__(self) -> None:
    '''Initialize the User database.'''
    # Connect to the database.
    self.con = sqlite3.connect('userdb.db')

    # Create a cursor to execute SQL commands.
    self.cur = self.con.cursor()

    # Create a table if not exists.
    self.cur.execute('''
    CREATE TABLE IF NOT EXISTS Userdb (
      "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
      "name" TEXT,
      "password" TEXT
      );''')

  def add_user(self, username='', password='') -> bool:
    '''Define a new user name and register its password.
    If the user name is already registered, a warning
    informs that the user name is not available.
    Return True it the user is registered. Otherwise, False.'''
    if username == '':
      print("Please, enter a valid name.")
      return False
    elif self.is_user(username):
      print("This name is already used.")
      return False
    else:
      statment = "INSERT INTO Userdb (name, password) VALUES (?,?);"
      self.cur.execute(statment, (username, password))
      
      create_table = '''
      CREATE TABLE IF NOT EXISTS ? (
      "noteId" INTEGER NOT NULL UNIQUE,
      "notes" TEXT,
      "tags" TEXT
      );'''

      # Create a table to record each note for the user.
      self.cur.execute(create_table, (username,))
      return True

  def add_notes(self, username, notes, noteId, tags ) -> None:
    '''Update the notes column of the database for the username specified.'''
    self.cur.execute('''
      INSERT INTO ? (noteId, notes, tags)
      VALUES (?, ?, ?);      
    ''', (username, noteId, notes, tags))
  
  def get_data(self, username="", password=""):
    '''Access user data from the user if the password is correct.'''
    self.cur.execute('''
      SELECT Userdb.name AND    
    ''')
  
  def is_user(self, username) -> bool:
    '''Function to verify an username.
    Returns False if its not registered.'''
    self.cur.execute('''
      SELECT name FROM Userdb WHERE name = ?;
    ''', (username,))

    query = self.cur.fetchall()
      
    if query == []:
      # Is not registered.
      return False
    if query[0][0] == username:
      return True

  def show_table(self):
    self.cur.execute('''
      SELECT * FROM Userdb;
    ''')
    print(self.cur.fetchall())

  def close(self):
    '''Save the changes persistently into the database and close its
    connection.'''
    self.con.commit()
    self.con.close()

userdb = None

def initialize_database():
  global userdb
  userdb = UserDB()
  print("User Database is initialized.")


#if "__name__" == "__main__":
initialize_database()
userdb.show_table()
userdb.add_user('Gwen', '108342')

#userdb.write_notes('Jymmy', "This is my first note!")
userdb.close()