#!/usr/bin/python
# Add location and Public Details to DataFileURI
# replace a string with another
# Usage: fandr.py "old" "new" file

import sys
import re
import glob

#rpstring = "<pi:ddi:DataFileURI>"
#psreplace1="  <r:Label>"+"\n"+"          <r:Content xml:lang=\"en-GB\">"
#psreplace2="</r:Content>"+"\n"+"        </r:Label>"+"\n"+"  "+str(rpstring)

renaming = open("renaming_list.txt",'r')
flocation={}
fpublic={}
for line in renaming:
  short,description,floc,fpub=line.split('\t')
  flocation[short.strip()]=floc.strip()
  fpublic[short.strip()]=fpub.strip()

for filename in glob.glob('*.ddi32.rp.xml'):
  fn=filename.split(".")
  location=str(flocation[fn[0]])
  pubfile=str(fpublic[fn[0]])
  rpstring = "<pi:DataFileURI>"+str(fn[0])+"</pi:DataFileURI>"
  psreplacement="<pi:DataFileURI isPublic=\""+str(pubfile)+"\">"+str(location)+"</pi:DataFileURI>"
  
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
