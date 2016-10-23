#!/net/edatools/algorete/2013.12/loopy/bin/python

import numpy as np
import sys


if __name__ == '__main__' : 
  files = [];
  fh = open('/l/disk0/work0/PauloH/Project2/results.csv', 'w');

  for arg in sys.argv: #interpret the argv
    if(arg[-4:] == '.csv'):
      files.append((arg[:-4], arg));

  for arg in files:
    print "Loading %s" % (arg[0][:]);
    data = np.loadtxt(arg[1]);
    line = "%s %s %s %s %s %s %s" % (arg[0], data[0], data[1], data[2], data[3], data[4], data[5]);
    fh.write(line + '\n');

  fh.close();
