import sys, os
import sqlite3
import argparse

root = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
dbpath = os.environ.get("CODE_TEST_DB")
if not dbpath:
  dbpath = root + '/code.db'

if len(sys.argv) == 1:
  print "Usage: " + sys.argv[0] + " -h"
  exit()

# perl perldoc   python pydoc
# perl File::Basename::basename  python 
# *) add a language '--add perl'
# *) list all the languages '--list'
# *) add a term in a language  '--add perl --term perldoc'

# *) delete a language if it does not have any phrases '--delete perl'

# *) connect two terms in two languages '--add perl perldoc python pydoc'
# *) query a term in a language and a target language '--ask perl perldoc python'
# *) query a term in a language '--ask perl perldoc'  listing all the other languages where it has a translation
# *) list all the terms in a language '--list perl'  listing all the terms in perl

# there should a version using a remote web-database
# but there could be a local version of it as well,
# maybe we caould allow mirroring the remote database (in read only mode)

def connect_to_database():
  global conn
  global c
  conn = sqlite3.connect(dbpath)
  c = conn.cursor()

  try:
    c.execute('''
      CREATE TABLE languages (
      id   INTEGER PRIMARY KEY,
      name VARCRCHAR(100) UNIQUE NOT NULL)''')
    c.execute('''
      CREATE TABLE phrases (
      id PRIMARY KEY,
      language INTEGER,
      text VARCRCHAR(200) NOT NULL)''')
    # should I set the language + text to be unique?
    c.execute('''
      CREATE TABLE translations (
      a INTEGER, b INTEGER)''')
    conn.commit()  
  except sqlite3.OperationalError, e:
    #print 'sqlite error: ', e.args[0]  # table companies already exists 
    pass
  pass

def delete_language(name):
  print 'Deleting ', name
  try:
    c.execute('''SELECT id, name FROM languages WHERE lower(name) = ?''', (name.lower(), ))
    lang = c.fetchone()
    if not lang:
      print 'The language is not in the database'
      return
    c.execute('''SELECT COUNT(*) FROM phrases WHERE language = ?''', (lang[0], ))
    counter = c.fetchone()
    #print counter
    print "Not yet implemented"
  except sqlite3.OperationalError, e:
    print 'sqlite error: ', e.args[0]  # table companies already exists 
    pass
    

def add_language(name):
  print 'Adding ', name
  #print name.lower()
  try:
    # TODO:
    # Avoid adding the same language twice in different case (e.g. alway check the lower case version) 
    # could be done with an SQL constraint?
    c.execute('''SELECT name FROM languages WHERE lower(name) = ?''', (name.lower(), ))
    exists = c.fetchone()
    if exists:
      print "Already in database as " + exists[0]
      return
    c.execute('''INSERT INTO languages (name) VALUES (?)''', (name,))
    conn.commit()
    print "Added"
  except sqlite3.IntegrityError, e:
    print 'sqlite error: ', e.args[0]

def list_languages():
  print 'Available languages'
  
  for language in c.execute('''SELECT name FROM languages'''):
    print language

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument('--add', help='add a language')
  #ap.add_argument('term', help='term')
  ap.add_argument('--delete', help='delete a language')
  ap.add_argument('--list', help='list the available languages', action='store_true')
  args = ap.parse_args()
  print args
  exit()

  connect_to_database()
  if args.add:
    add_language(args.add)
  elif args.delete:
    delete_language(args.delete)
  elif args.list:
    list_languages()
  else:
    print "Usage: " + sys.argv[0] + " -h"

  conn.close()
  #print args
  #print args["add"]
#  ap.add_argument('--from', help='language from')
#  ap.add_argument('--to',   help='language to')
#  ap.add_argument('--term', help='the term')
  
  
main()
