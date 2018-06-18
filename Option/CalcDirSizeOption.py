# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import os, sys
import threadpool
from Option.Option import Option
from FileInfo.FileInfoCatcher import FileInfoCatcher

class CalcDirSizeOption(Option):

    def __init__(self, toCalc):
        super().__init__()
        self.toCalc = toCalc

    def execute(self, obj):
        self.obj = obj
        self.fileInfoCatcher = FileInfoCatcher()
        if self.toCalc.lower() == 'true':
            for fullName in self.obj:
                if self.obj[fullName]['isDir']:
                    FileInfoCatcher.calcDirThreadPool.putRequest(
                        threadpool.makeRequests(
                            self.fileInfoCatcher.calcSize,
                            [
                                (
                                    (fullName, self.obj),
                                    None
                                ),
                            ]
                        )[0]
                    )
            FileInfoCatcher.calcDirThreadPool.wait()

        elif self.toCalc.lower() == 'false':
            pass
        else:
            print('[Error] 错误参数:', self.toCalc)
            sys.exit(0)

        return self.obj


