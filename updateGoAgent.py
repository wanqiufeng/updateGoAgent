__author__ = 'vincent'
import sys
import requests
import re
import bs4


global remoteVersionNo
global downloadAddr


def downloadNewVersion():
    print("new version download")
nticat

def replaceOldVersion():
    pass


def addAppID():
    pass


def deploy():
    pass


def hasNewVersion():
    if getLocalVersion():
        return True
    return False


def getLocalVersion():
    with open('local/proxy.py', 'rt') as f:
        for line in f:
            if "__version__" in line:
                return (eval(line[line.index("=") + 1:]))


def getRemoteVersionInfo():
    r = requests.get('https://code.google.com/p/goagent/')
    soup = bs4.BeautifulSoup(r.text)

    #get remote version no
    remoteVersionNoStr = str(soup.p.find(text=True))
    matchVersion = re.search('goagent (.+?) 正式版下载',remoteVersionNoStr)
    remoteVersionNo = matchVersion.group(1)
    print(remoteVersionNo)

    #get remote version download address
    downloadAddr = str(soup.p.a['href'])
    print(downloadAddr)

def main():
    getRemoteVersionInfo()
    if hasNewVersion():
        downloadNewVersion()


if __name__ == '__main__':
    main()
