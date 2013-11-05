__author__ = 'vincentc'
import os
with open('local/proxy.py', 'rt') as f:
        for line in f:
            if "__version__" in line:
                print(line[line.index("=")+1:])
                break


