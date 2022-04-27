#This is the data pipeline using python

import sys
for line in sys.stdin:
  1st3 = line[0:3]
  2nd3 = line[3:6]
  residue = line[6:]
  print('(',1st3,')-',2nd3,'-',residue)
