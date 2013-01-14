import sys
import sqlite3
import argparse

dbpath = 'code.db'

# perl perldoc   python pydoc
# perl File::Basename::basename  python 
# 1) add a term in a language  '--add perl perldoc'
# 2) connect two terms in two languages '--add perl perldoc python pydoc'
# 3) query a term in a language and a target language '--ask perl perldoc python'
# 4) query a term in a language '--ask perl perldoc'  listing all the other languages where it has a translation
# 5) list all the terms in a language '--list perl'  listing all the terms in perl
# 6) list all the languages --list
# 7) add a language '--add perl'

# there should a version using a remote web-database
# but there could be a local version of it as well,
# maybe we caould allow mirroring the remote database (in read only mode)

def connect_to_database():
  pass

def add_language(name):
  print 'Adding ', name

def list_languages():
  print 'Available languages'

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument('--add', help='add a language')
  ap.add_argument('--list', help='list the available languages', action='store_true')
  args = ap.parse_args()
  if args["add"]:
    add_language(args["add"])
  if args["list"]:
    list_languages()
    
  #print args
  #print args["add"]
#  ap.add_argument('--from', help='language from')
#  ap.add_argument('--to',   help='language to')
#  ap.add_argument('--term', help='the term')
  
  
  

main()