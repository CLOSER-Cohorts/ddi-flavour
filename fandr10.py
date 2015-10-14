#!/usr/bin/python
# Correct Invalid to InvalidCases in SummaryStatistics
# replace a string with another
# Usage: fandr.py "old" "new" file

import sys
import re
import glob

oldstring = "<pi:TypeOfSummaryStatistic>Invalid"
newstring = "<pi:TypeOfSummaryStatistic>InvalidCases"

for filename in glob.glob('*.ddi32.rp.xml'):
  try:
    s = open(filename).read()
  except IOError:
    print "No such file"
    sys.exit(2)
  
  # Well, we've got this far - the file must exist!
  if oldstring in s:
    s=s.replace(oldstring,newstring)
    
    f=open(filename, "w")
    f.write(s)
    f.flush()
    f.close()
      
  else:
    print "No occurences of "+ str(oldstring) +" found.in "+str(filename)
