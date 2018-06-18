# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import sys
from functools import cmp_to_key

class OptionParser(object):

    optionOrderType = {
        '-calcDirSize'.lower(): -1,
        '-mode'.lower(): 0,
        '-include'.lower(): 1,
        '-maxSize'.lower(): 2,
        '-minSize'.lower(): 2,
        '-sort'.lower(): 3,
    }

    def __init__(self):
        super().__init__()

    @staticmethod
    def parse(option):
        isMode = OptionParser.__check(option)
        return (
            sorted(
                list(zip(option[::2], option[1::2])),
                key=cmp_to_key(
                    lambda x, y:
                    OptionParser.optionOrderType[x[0].lower()]
                    - OptionParser.optionOrderType[y[0].lower()]
                )
            ), isMode
        )

    @staticmethod
    def __check(option):
        it = iter(option)
        isMode = False

        if '-mode'.lower() in [op.lower() for op in option]:
            if len(option) != 2:
                print('[Error] -mode log 或 -mode diff只能单独使用')
                sys.exit(0)
            else:
                isMode = True

        while True:
            try:
                option1 = next(it)
                if option1[0] != '-':
                    print(
                        '[Error] 命令行选项-type operate, type以"-"开头, 错误值:',
                        option1
                    )
                    sys.exit(0)
            except StopIteration:
                # 遇到StopIteration就退出循环
                break

            try:
                option2 = next(it)
                if option2 == '-':
                    print(
                        '[Error] 命令行选项-type operate, operate不能以"-"开头, 错误值:',
                        option2
                    )
                    sys.exit(0)
            except StopIteration:
                print(
                    '[Error] 命令行选项-type operate, operate值缺失',
                )
                sys.exit(0)

        return isMode

