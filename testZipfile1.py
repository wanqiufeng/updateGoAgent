__author__ = 'vincentc'
import zipfile
import os
import shutil
localDirectory = None
serverDirectory = None
goagentZip = zipfile.ZipFile('goagent-goagent-v3.0.6-10-g52684c0.zip', 'r')

for name in goagentZip.namelist():
    print(name)