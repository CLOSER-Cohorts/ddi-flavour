#!/usr/bin/python
#< replace a string with another
# Usage: fandr.py "old" "new" file

import sys
import re
import glob

rpstring = "<ddi:LogicalRecord "
psreplace1="  <ddi:DataRelationshipName>"+"\n"+"         <r:String xml:lang=\"en-GB\">"
psreplace2="</r:String>"+"\n"
psreplace3="        </ddi:DataRelationshipName>"+"\n"+"  "+str(rpstring)

renaming = open("renaming_list.txt",'r')
newdict={}
for line in renaming:
	short,description,floc,fpub=line.split('\t')
	newdict[short.strip()]=description.strip()
for filename in glob.glob('*.ddi32.rp.xml'):
  fn=filename.split(".")
  instnames=str(fn[0])
  instnamel=str(newdict[fn[0]])+" Data Relationship Name"
  psreplacement=psreplace1+instnamel+psreplace2+psreplace3  
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
