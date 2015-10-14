#!/usr/bin/python
# Add PhysicalDataProductNam
# replace a string with another
# Usage: fandr.py "old" "new" file

import sys
import re
import glob

rpstring = "<p:PhysicalStructureScheme"
psreplace1="  <p:PhysicalDataProductName>"+"\n"+"       <r:String xml:lang=\"en-GB\">"
psreplace2="</r:String>"+"\n"+"      </p:PhysicalDataProductName>"+"\n"+"    "+str(rpstring)

newdict={}

for filename in glob.glob('*.ddi32.rp.xml'):
  fn=filename.split(".")
  instname=str(fn[0])
  psreplacement=psreplace1+instname+psreplace2  
  try:
    s = open(filename).read()
  except IOError:
    print "No such file"
    sys.exit(2)
  # Well, we've got this far - the file must exist!
  if rpstring in s:
    s=s.replace(rpstring,psreplacement,1)
    
    f=open(filename, "w")
    f.write(s)
    f.flush()
    f.close()
      
  else:
    print "No occurences of "+ str(rpstring) +" found.in "+str(filename)
