__author__ = 'vincentc'
import zipfile
import os
import shutil
localDirectory = None
serverDirectory = None
goagentZip = zipfile.ZipFile('goagent-goagent-v3.0.6-10-g52684c0.zip', 'r')
#goagentZip.printdir()
zipNameList = goagentZip.namelist()
shutil.rmtree("server")
dir = os.mkdir("server")
for name in zipNameList:
    if name.endswith("local/"):
        localDirectory = name
    if name.endswith("server/"):
        serverDirectory = name
    if "server/" in name and not name.endswith("/"):
        print(name)
        source = goagentZip.open(name)
        shutil.copyfileobj(source,)

#print(goagentZip.namelist())

#goagentZip.extract(localDirectory+"proxy.py")
#goagentZip.extractall()