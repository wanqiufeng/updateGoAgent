__author__ = 'vincent'
import sys
import requests
import re
import bs4
global newVersionNo
global downloadAddr
def downloadNewVersion():
    print("new version download")
def replaceOldVersion():
    pass
def addAppID():
    pass
def deploy():
    pass
def hasNewVersion():
    if getLocalVersion() != getRemoteVersion():
        return True
    return False

def getLocalVersion():
    with open('local/proxy.py', 'rt') as f:
            for line in f:
                if "__version__" in line:
                    return(eval(line[line.index("=")+1:]))

def getRemoteVersionInfo():
    r = requests.get('https://code.google.com/p/goagent/')
    result = r.text
    match = re.search('<p>(.*)</p>',result)
    matchVersion = re.search('goagent (.+?) 正式版下载',match.group(0))
    newVersionNo = matchVersion.group(1)


def main():
    if hasNewVersion():
        downloadNewVersion()
if __name__ == '__main__':
   main()
