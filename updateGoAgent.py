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


g_remoteVersionNo = None
g_downloadAddr = None
g_fileName = None
g_appID = None

def downloadNewVersion():
    global g_fileName
    r = requests.get(g_downloadAddr, stream=True,verify=False)
    g_fileName = getFileName(r.headers.get('content-disposition'))
    with open(g_fileName, 'wb') as fd:
        for chunk in r.iter_content(1024):
            fd.write(chunk)
    #TO_DO: 1. change fixed download file to temp file
    #TO_DO: 2.add download percent show
def getFileName(str):
    return str[str.index("=")+1:]

def addAppID():
    configparser.ConfigParser.OPTCRE = re.compile(r'(?P<option>[^=\s][^=]*)\s*(?P<vi>[=])\s*(?P<value>.*)$')
    config = configparser.ConfigParser()
    config['gae']['appid'] = "wanqiufeng1"
    with open('local/proxy.ini', 'a') as configfile:
        config.write(configfile)

def deploy():
    os.system(".\\server\\uploader.bat")


def hasNewVersion():
    if getLocalVersion() == g_remoteVersionNo:
        return False
    return True


def getLocalVersion():
    with open('local/proxy.py', 'rt') as f:
        for line in f:
            if "__version__" in line:
                return (eval(line[line.index("=") + 1:]))


def getLocalAppId():
    global g_appID
    configparser.ConfigParser.OPTCRE = re.compile(r'(?P<option>[^=\s][^=]*)\s*(?P<vi>[=])\s*(?P<value>.*)$')
    config = configparser.ConfigParser()
    config.read('local/proxy.ini')
    g_appID = config["gae"]["appid"]

def getRemoteVersionInfo():
    global g_remoteVersionNo
    global g_downloadAddr
    r = requests.get('https://code.google.com/p/goagent/')
    soup = bs4.BeautifulSoup(r.text)

    #get remote version no
    remoteVersionNoStr = str(soup.p.find(text=True))
    matchVersion = re.search('goagent (.+?) 正式版下载',remoteVersionNoStr)
    g_remoteVersionNo = matchVersion.group(1)

    #get remote version download address
    g_downloadAddr = str(soup.p.a['href'])

def replaceOldVersion():
    goagentZip = zipfile.ZipFile("goagent-goagent-v3.0.6-10-g52684c0.zip", 'r')
    goagentSubFolder_Server = "server/"
    goagentSubFolder_Local = "local/"
    createFolder(goagentSubFolder_Server,True)
    createFolder(goagentSubFolder_Local,True)
    for name in goagentZip.namelist():
        if (goagentSubFolder_Server in name or goagentSubFolder_Local in name ) and not name.endswith("/"):
            folderIndex = None
            if goagentSubFolder_Local in name:
                folderIndex = name.find(goagentSubFolder_Local)
            elif goagentSubFolder_Server in name:
                folderIndex = name.find(goagentSubFolder_Server)

            relatedPath = name[folderIndex:len(name)]
            createFolder(os.path.dirname(relatedPath),False)
            with open(relatedPath,"wb") as tempfile:
                shutil.copyfileobj(goagentZip.open(name),tempfile)

def createFolder(folderName,override=False):
    if os.path.isdir(folderName) and override:
        shutil.rmtree(folderName)
    os.makedirs(folderName,exist_ok=True)

def main():
    #getRemoteVersionInfo()
    #downloadNewVersion()
    #overrideOldFile()
    #if hasNewVersion():
        #downloadNewVersion()
    #getLocalAppId()
    addAppID()

if __name__ == '__main__':
    main()
