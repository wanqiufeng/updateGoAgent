__author__ = 'vincent'
import sys
import requests
import re
import bs4


remoteVersionNo = None
downloadAddr = None


def downloadNewVersion():
    print(downloadAddr)
    r = requests.get(downloadAddr, stream=True,verify=False)
    print(r.headers.get('content-disposition'))
    #with open("fff", 'wb') as fd:
        #for chunk in r.iter_content(1024):
            #fd.write(chunk)
def replaceOldVersion():
    pass


def addAppID():
    pass


def deploy():
    pass


def hasNewVersion():
    if getLocalVersion() == remoteVersionNo:
        return False
    return True


def getLocalVersion():
    with open('local/proxy.py', 'rt') as f:
        for line in f:
            if "__version__" in line:
                return (eval(line[line.index("=") + 1:]))


def getRemoteVersionInfo():
    global remoteVersionNo
    global downloadAddr
    r = requests.get('https://code.google.com/p/goagent/')
    soup = bs4.BeautifulSoup(r.text)

    #get remote version no
    remoteVersionNoStr = str(soup.p.find(text=True))
    matchVersion = re.search('goagent (.+?) 正式版下载',remoteVersionNoStr)
    remoteVersionNo = matchVersion.group(1)

    #get remote version download address
    downloadAddr = str(soup.p.a['href'])

def main():
    getRemoteVersionInfo()
    downloadNewVersion()
    #if hasNewVersion():
        #downloadNewVersion()


if __name__ == '__main__':
    main()
