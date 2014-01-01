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


def downloadNewVersion(downloadAddr,proccessBar):
    print("starting download ...")
    r = requests.get(downloadAddr, stream=True, verify=False)
    totalFileLength = int((r.headers.get("Content-Length").strip()))
    downLoadSize = 0
    previousPercent = 0
    tempFile = tempfile.TemporaryFile()
    print("starting writing file...")
    for chunk in r.iter_content(1024):
        #downLoadSize += len(chunk)
        proccessBar.step(len(chunk)/ totalFileLength*100)
        #proccessBar.step(math.floor((downLoadSize / totalFileLength) * 100))
        tempFile.write(chunk)
    return tempFile
    #TO_DO: 1. change fixed download file to temp file
    #TO_DO: 2.add download percent show




def setAppID(appId,path):
    configparser.ConfigParser.OPTCRE = re.compile(r'(?P<option>[^=\s][^=]*)\s*(?P<vi>[=])\s*(?P<value>.*)$')
    config = configparser.ConfigParser()
    path_abs_proxyINI = os.path.join(os.path.dirname(path),"proxy.ini")
    config.read(path_abs_proxyINI)
    config.remove_option("gae", "appid")
    config.set("gae", "appid", appId)
    with open(path_abs_proxyINI, 'w') as configfile:
        config.write(configfile)


def deploy():
    os.system(".\\server\\uploader.bat")


def hasNewVersion(localVersion, remoteVersion):
    if localVersion == remoteVersion:
        return False
    return True


def getLocalVersion(path):
    #with open('local/proxy.py', 'rt') as f:
    with open(os.path.join(os.path.dirname(path),"proxy.py"), 'rt') as f:
        for line in f:
            if "__version__" in line:
                return (eval(line[line.index("=") + 1:]))


def getAppId(path):
    configparser.ConfigParser.OPTCRE = re.compile(r'(?P<option>[^=\s][^=]*)\s*(?P<vi>[=])\s*(?P<value>.*)$')
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(path),"proxy.ini"))
    appID = config["gae"]["appid"]
    return appID


def getRemoteVersionInfo():
    r = requests.get('https://code.google.com/p/goagent/',verify=False)
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


def replaceOldVersion(newZipFileName,path):
    path_abs_root = os.path.dirname(os.path.dirname(path))
    path_obs_server = os.path.join(path_abs_root,"server")
    path_obs_local = os.path.join(path_abs_root,"local")
    goagentZip = zipfile.ZipFile(newZipFileName, 'r')
    path_relative_server = "server/"
    path_relative_local = "local/"
    createFolder(path_obs_server, True)
    createFolder(path_obs_local, True)
    for name in goagentZip.namelist():
        if (path_relative_server in name or path_relative_local in name ) and not name.endswith("/"):
            folderIndex = None
            if path_relative_local in name:
                folderIndex = name.find(path_relative_local)
            elif path_relative_server in name:
                folderIndex = name.find(path_relative_server)

            relatedPath = name[folderIndex:len(name)]
            absolutePath = os.path.join(path_abs_root,relatedPath)
            createFolder(os.path.dirname(absolutePath), False)
            with open(absolutePath, "wb") as tempfile:
                shutil.copyfileobj(goagentZip.open(name), tempfile)


def createFolder(folderName, override=False):
    if os.path.isdir(folderName) and override:
        shutil.rmtree(folderName)
    os.makedirs(folderName, exist_ok=True)

def main(path,tipsLabel,proccessBar,vAppId,btnUpdate,etyAppId):
    tipsLabel.set("get Remote Version Info ...")
    remoteInfo = getRemoteVersionInfo()
    tipsLabel.set("get Local App ID ...")
    tipsLabel.set("judge whether need update ...")
    if hasNewVersion(getLocalVersion(path), remoteInfo["remoteVersionNo"]):
        tipsLabel.set("download new version ...")
        downloadedFile = downloadNewVersion(remoteInfo["downloadAddr"],proccessBar)
        tipsLabel.set("replace old version ...")
        replaceOldVersion(downloadedFile,path)
        tipsLabel.set("set appid id ...")
        setAppID(vAppId.get(),path)
        tipsLabel.set("delete  download file ... ")
        downloadedFile.close()
        tipsLabel.set("update completed.")
        proccessBar.grid_remove()
        btnUpdate.state(['!disabled'])
        etyAppId.state(['!disabled'])

def test():
    #print("already downLoad ", math.floor((6565654 / 4724570) * 100))
    #getAppId("C:/Users/vincent/Documents/GitHub/updateGoAgent/local/goagent.exe")
    print(getAppId("C:/Users/vincent/Documents/GitHub/updateGoAgent/local/goagent.exe"))

if __name__ == '__main__':
    main("C:/Users/vincent/Documents/GitHub/updateGoAgent/local/goagent.exe")
    #test()
