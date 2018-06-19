# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import time, os, sys
from FileInfo.FileInfoCatcher import FileInfoCatcher
from Option.OptionParser import OptionParser
from Option.OptionFactory import OptionFactory
from Option.Option import Options
from Option.HelpOption import HelpOption

class OodleApp(object):
    def __init__(self, queryPath, optionStr):
        super().__init__()

        self.queryPath = queryPath
        self.optionStr = optionStr

        self.run()

    def run(self):
        if not os.path.exists(self.queryPath) and self.queryPath != '':
            print('[Error] 不存在路径:', self.queryPath)
            sys.exit(0)
        if self.queryPath == '-help' or self.queryPath == '':
            HelpOption().execute()
            return

        fileInfoCatcher = FileInfoCatcher()
        self.fileInfo = fileInfoCatcher.getDirInfo(self.queryPath)

        optionList, isMode = OptionParser.parse(self.optionStr)
        optionFactory = OptionFactory()
        options = Options()

        if not isMode:
            for op in optionList:
                option = optionFactory.createOption(op)
                options.addOption(option(op[1]))

            self.fileInfo = options.execute(self.fileInfo)

        else:
            for op in optionList:
                option = optionFactory.createOption(op)
                options.addOption(option())

            self.fileInfo = options.execute(self.queryPath)

        self.prettifyPrint(self.fileInfo)

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

    def prettifyPrint(self, fileInfo):
        if fileInfo == None:
            return

        print('查看路径:', self.queryPath)
        print('============================')
        print('    修改时间', '         文件大小', '      类型', '       文件名')
        for key, value in fileInfo.items():
            print(
                self.__prettifyDate(value['modifyTime']) + '   ',
                self.__prettifySize(value['size']).ljust(13, ' '),
                '<dir>    ' if value['isDir'] else '<file>   ',
                value['name'],
            )
