import sys, os
import subprocess
import tempfile
import re

root = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
command = root +  '/bin/codetionary.py'
print 'Command: ' + command

dir = tempfile.mkdtemp()
dbfile = dir + '/test.db'
print 'DBfile: ' + dbfile

os.environ["CODE_TEST_DB"] = dbfile

#p = subprocess.Popen([sys.executable, '-V'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
p = subprocess.Popen([sys.executable, command], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
stdout,stderr = p.communicate()


def ok(truth, name):
  global ok_counter
  ok_counter = 0
  if ok_counter == None:
    ok_counter = 0
  ok_counter += 1
  if not truth:
    print 'not ',
  print 'ok', ok_counter,
  if not name == None:
    print name,
  print ''

#print stdout
ok(stderr == '', 'stderr')

# delete the file and the directory as well
# os.unlink()

os.rmdir(dir)

