#!/usr/bin/python
# Add Title to Resource Package
# replace a string with another
# Usage: fandr.py "old" "new" file

import sys
import re
import glob

delstring="    <r:Purpose>\n      <r:Content/>\n    </r:Purpose>"
rpstring = "<ddi:LogicalProduct "
psreplace1="  <r:Citation>"+"\n"+"          <r:Title><r:String xml:lang=\"en-GB\">"
psreplace2="</r:String></r:Title>"+"\n"
psreplace3="          <r:AlternateTitle><r:String xml:lang=\"en-GB\">"
psreplace4="</r:String></r:AlternateTitle>"+"\n"
psreplace5="        </r:Citation>"+"\n"+"  "+str(rpstring)

renaming = open("renaming_list.txt",'r')
newdict={}
for line in renaming:
	short,description,floc,fpub=line.split('\t')
	newdict[short.strip()]=description.strip()

for filename in glob.glob('*.ddi32.rp.xml'):
  fn=filename.split(".")
  instnames=str(fn[0])
  try:
    instnamel=str(newdict[fn[0]])+" Resource Package"
  except KeyError:
    print "filename" + instnames + " in renaming file does not match data file"
    sys.exit(2)
    	
  psreplacement=psreplace1+instnamel+psreplace2+psreplace3+instnames+psreplace4+psreplace5  
  try:
    s = open(filename).read()
  except IOError:
    print "No such file"
    sys.exit(2)
  
  # Well, we've got this far - the file must exist!
  if rpstring in s:
    s=s.replace(rpstring,psreplacement)

  if delstring in s:
    s=s.replace(delstring,"")
    
    f=open(filename, "w")
    f.write(s)
    f.flush()
    f.close()
      
  else:
    print "No occurences of "+ str(rpstring) +" found.in "+str(filename)
