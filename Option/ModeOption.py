# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import os, sys
import time
import pickle
import threadpool
from Option.Option import Option
from FileInfo.FileInfoCatcher import FileInfoCatcher

if not os.path.exists('Log'):
    os.mkdir('Log/')

class LogModeOption(Option):
    def __init__(self):
        super().__init__()

    def execute(self, path):
        fileInfoCatcher = FileInfoCatcher()
        fileInfo = fileInfoCatcher.getDirInfo(path)

        for fullName in fileInfo:
            if fileInfo[fullName]['isDir']:
                FileInfoCatcher.calcDirThreadPool.putRequest(
                    threadpool.makeRequests(
                        fileInfoCatcher.calcSize,
                        [
                            (
                                (fullName, fileInfo),
                                None
                            ),
                        ]
                    )[0]
                )
        FileInfoCatcher.calcDirThreadPool.wait()

        with open('Log/'
                  + path.replace('/', '').replace('\\', '').replace(':', '')
                  + '.pickle', 'wb') as f:
            pickle.dump(fileInfo, f)

        return fileInfo


class DiffModeOption(Option):
    def __init__(self):
        super().__init__()

    def execute(self, path):
        pathKey = 'Log/' \
                  + path.replace('/', '').replace('\\', '').replace(':', '') \
                  + '.pickle'

        if not os.path.exists(path):
            print('[Error] 目录的日志不存在, 请以日志模式运行.目录:', path)
            sys.exit(0)

        fileInfoCatcher = FileInfoCatcher()
        fileInfo = fileInfoCatcher.getDirInfo(path)

        for fullName in fileInfo:
            if fileInfo[fullName]['isDir']:
                FileInfoCatcher.calcDirThreadPool.putRequest(
                    threadpool.makeRequests(
                        fileInfoCatcher.calcSize,
                        [
                            (
                                (fullName, fileInfo),
                                None
                            ),
                        ]
                    )[0]
                )
        FileInfoCatcher.calcDirThreadPool.wait()

        with open(pathKey, 'rb') as f:
            logFileInfo = pickle.load(f)

        logFileSet = set(logFileInfo)
        diffFileSet = set(fileInfo)

        newFileSet = diffFileSet - logFileSet
        deleteFileSet = logFileSet - diffFileSet
        commonFileSet = diffFileSet & logFileSet

        self.showDiff(path, newFileSet, deleteFileSet, commonFileSet, logFileInfo, fileInfo)

        with open(pathKey, 'wb') as f:
            pickle.dump(fileInfo, f)

        return None

    def __prettifySize(self, size):
        size = float(size)
        if size >= 1024 * 1024 * 1024:
            return '%.3fGB' % (size / 1024 / 1024 / 1024)
        elif size >= 1024 * 1024:
            return '%.3fMB' % (size / 1024 / 1024)
        elif size >= 1024:
            return '%.3fKB' % (size / 1024)
        else:
            return '%.3fB ' % size

    def __prettifyDate(self, date):
        return time.strftime('%F %X', time.localtime(date))

    def showDiff(self, path, newFileSet, deleteFileSet, commonFileSet, logFileInfo, fileInfo):
        print('查看的目录:', path)
        if len(newFileSet):
            print('=' * 50)
            print('新增的文件(子目录):')
            print('    修改时间', '         文件大小', '      类型', '       文件名')
            for newFile in newFileSet:
                print(
                    self.__prettifyDate(fileInfo[newFile]['modifyTime']) + '   ',
                    self.__prettifySize(fileInfo[newFile]['size']).ljust(13, ' '),
                    '<dir>    ' if fileInfo[newFile]['isDir'] else '<file>   ',
                    fileInfo[newFile]['name'],
                )
        if len(deleteFileSet):
            print('=' * 50)
            print('被删除的文件(子目录):')
            print('    修改时间', '         文件大小', '      类型', '       文件名')
            for deleteFile in deleteFileSet:
                print(
                    self.__prettifyDate(logFileInfo[deleteFile]['modifyTime']) + '   ',
                    self.__prettifySize(logFileInfo[deleteFile]['size']).ljust(13, ' '),
                    '<dir>    ' if logFileInfo[deleteFile]['isDir'] else '<file>   ',
                    logFileInfo[deleteFile]['name'],
                )
        if len(commonFileSet):
            print('=' * 50)
            print('有变化的文件(子目录):')
            print('    修改时间', '         文件大小', '      类型', '       文件名')
            for commonFile in commonFileSet:
                if logFileInfo[commonFile]['modifyTime'] != fileInfo[commonFile]['modifyTime']:
                    print(
                        self.__prettifyDate(logFileInfo[commonFile]['modifyTime']) + '   ',
                        self.__prettifySize(logFileInfo[commonFile]['size']).ljust(13, ' '),
                        '<dir>    ' if logFileInfo[commonFile]['isDir'] else '<file>   ',
                        logFileInfo[commonFile]['name'],
                    )