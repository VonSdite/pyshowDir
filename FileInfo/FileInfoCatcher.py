# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import os
import threading
import threadpool

class FileInfoCatcher(object):
    calcDirThreadPool = threadpool.ThreadPool(10)
    _instanceLock = threading.Lock()

    def __init__(self):
        super().__init__()

    def __new__(cls, *args, **kwargs):
        if not hasattr(FileInfoCatcher, "_instance"):
            with FileInfoCatcher._instanceLock:
                if not hasattr(FileInfoCatcher, "_instance"):
                    FileInfoCatcher._instance = object.__new__(cls)
        return FileInfoCatcher._instance

    def getDirInfo(self, path):
        fileInfo = dict()
        for f in os.listdir(path):
            fullName = os.path.join(path, f)

            fileInfo[fullName] = dict(
                name=f,
                fullName=fullName,
                size=os.stat(fullName).st_size if not os.path.isdir(fullName) else 0,
                modifyTime=os.stat(fullName).st_mtime,
                isDir=os.path.isdir(fullName)
            )

        return fileInfo

    def calcSize(self, path, obj=None):
        if (os.path.isdir(path)):
            size = 0
            for root, dirs, files in os.walk(path):
                for f in files:
                    try:
                        size += os.stat(os.path.join(root, f)).st_size
                    except:
                        pass

            if obj != None:
                obj[path]['size'] = size
            return size
        else:
            return os.stat(path).st_size




