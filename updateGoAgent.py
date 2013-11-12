__author__ = 'vincent'
import sys
import requests
import re
import bs4
import tempfile
import zipfile
import os
import shutil
import configparser
import math


def downloadNewVersion(downloadAddr):
    r = requests.get(downloadAddr, stream=True, verify=False)
    fileName = getFileName(r.headers.get('content-disposition'))
    totalFileLength = int((r.headers.get("Content-Length").strip()))
    downLoadSize = 0
    previousPercent = 0
    with open(fileName, 'wb') as fd:
        for chunk in r.iter_content(1024):
            downLoadSize += len(chunk)
            fd.write(chunk)
            printProccess(math.floor((downLoadSize / totalFileLength) * 100),previousPercent)
            previousPercent = math.floor((downLoadSize / totalFileLength) * 100)
    return fileName
    #TO_DO: 1. change fixed download file to temp file
    #TO_DO: 2.add download percent show


def printProccess(currentNum,PreviouseNum):
    if currentNum > PreviouseNum:
        print("#",end='')
def getFileName(str):
    return str[str.index("=") + 1:]


def setAppID(appId):
    configparser.ConfigParser.OPTCRE = re.compile(r'(?P<option>[^=\s][^=]*)\s*(?P<vi>[=])\s*(?P<value>.*)$')
    config = configparser.ConfigParser()
    config.read('local/proxy.ini')
    config.remove_option("gae", "appid")
    config.set("gae", "appid", appId)
    with open('local/proxy.ini', 'w') as configfile:
        config.write(configfile)


def deploy():
    os.system(".\\server\\uploader.bat")


def hasNewVersion(localVersion, remoteVersion):
    if localVersion == remoteVersion:
        return False
    return True


def getLocalVersion():
    with open('local/proxy.py', 'rt') as f:
        for line in f:
            if "__version__" in line:
                return (eval(line[line.index("=") + 1:]))


def getAppId():
    configparser.ConfigParser.OPTCRE = re.compile(r'(?P<option>[^=\s][^=]*)\s*(?P<vi>[=])\s*(?P<value>.*)$')
    config = configparser.ConfigParser()
    config.read('local/proxy.ini')
    appID = config["gae"]["appid"]
    return appID


def getRemoteVersionInfo():
    r = requests.get('https://code.google.com/p/goagent/')
    soup = bs4.BeautifulSoup(r.text)

    #get remote version no
    remoteVersionNoStr = str(soup.p.find(text=True))
    matchVersion = re.search('goagent (.+?) 正式版下载', remoteVersionNoStr)
    remoteVersionNo = matchVersion.group(1)

    #get remote version download address
    downloadAddr = str(soup.p.a['href'])
    return {
        "remoteVersionNo": remoteVersionNo,
        "downloadAddr": downloadAddr
    }


def replaceOldVersion(newZipFileName):
    goagentZip = zipfile.ZipFile(newZipFileName, 'r')
    goagentSubFolder_Server = "server/"
    goagentSubFolder_Local = "local/"
    createFolder(goagentSubFolder_Server, True)
    createFolder(goagentSubFolder_Local, True)
    for name in goagentZip.namelist():
        if (goagentSubFolder_Server in name or goagentSubFolder_Local in name ) and not name.endswith("/"):
            folderIndex = None
            if goagentSubFolder_Local in name:
                folderIndex = name.find(goagentSubFolder_Local)
            elif goagentSubFolder_Server in name:
                folderIndex = name.find(goagentSubFolder_Server)

            relatedPath = name[folderIndex:len(name)]
            createFolder(os.path.dirname(relatedPath), False)
            with open(relatedPath, "wb") as tempfile:
                shutil.copyfileobj(goagentZip.open(name), tempfile)


def createFolder(folderName, override=False):
    if os.path.isdir(folderName) and override:
        shutil.rmtree(folderName)
    os.makedirs(folderName, exist_ok=True)


def deleteFile(fileName):
    os.remove(fileName)


def main():
    remoteInfo = getRemoteVersionInfo()
    localAppId = getAppId()
    if hasNewVersion(getLocalVersion(), remoteInfo["remoteVersionNo"]):
        fileName = downloadNewVersion(remoteInfo["downloadAddr"])
        replaceOldVersion(fileName)
        setAppID(localAppId)
        deleteFile(fileName)
        deploy()


def test():
    print("already downLoad ", math.floor((6565654 / 4724570) * 100))

if __name__ == '__main__':
    main()
    #test()
