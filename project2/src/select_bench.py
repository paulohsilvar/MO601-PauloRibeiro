#!/net/edatools/algorete/2013.12/loopy/bin/python

import numpy as np
import sys


if __name__ == '__main__' : 
  files = [];
  max = [];
  select = [];

  for arg in sys.argv: #interpret the argv
    if(arg[-4:] == '.csv'):
      files.append((arg[:-4], np.loadtxt(arg)));

  for f in files:
    max.append((f[1][3], f[0]));

  max.sort();
  max = max[::-1];

  for m in max:
    if(not(m[1] in select)):
      select.append(m[1]);
    

  print select;

