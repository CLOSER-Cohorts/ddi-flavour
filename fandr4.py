#!/usr/bin/python
# Adds LogicalProductName
# replace a string with another
# Usage: fandr.py "old" "new" file

import sys
import re
import glob

rpstring = "<ddi:DataRelationship "
psreplace1="  <r:Label xmlns=\"ddi:reusable:3_2\">"+"\n"+"      <r:Content xml:lang=\"en-GB\">"
psreplace2="</r:Content>"+"\n"+"  </r:Label>"+"\n"+"  "+str(rpstring)

renaming = open("renaming_list.txt",'r')
newdict={}
for line in renaming:
	short,description,floc,fpub=line.split('\t')
	newdict[short.strip()]=description.strip()


for filename in glob.glob('*.ddi32.rp.xml'):
  fn=filename.split(".")
  try:
    instname=str(newdict[fn[0]])+" Logical Product" 
  except KeyError:
    print "filename" + instnames + " in renaming file does not match data file"
    sys.exit(2)

 
  psreplacement=psreplace1+instname+psreplace2  
  try:
    s = open(filename).read()
  except IOError:
    print "No such file"
    sys.exit(2)
  
  # Well, we've got this far - the file must exist!
  if rpstring in s:
    s=s.replace(rpstring,psreplacement)
    
    f=open(filename, "w")
    f.write(s)
    f.flush()
    f.close()
      
  else:
    print "No occurences of "+ str(rpstring) +" found.in "+str(filename)
