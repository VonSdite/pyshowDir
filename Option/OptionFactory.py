# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

from Option.SizeOption import *
from Option.SortOption import *
from Option.ModeOption import *
from Option.CalcDirSizeOption import *
from Option.NameIncludeOption import *
import sys

class OptionFactory(object):

    def __init__(self):
        super().__init__()

    def createOption(self, option):

        if option[0].lower() == '-sort'.lower():
            if option[1].lower()[:6] == 'byName'.lower():
                return SortByNameOption
            elif option[1].lower()[:6] == 'bySize'.lower():
                return SortBySizeOption
            elif option[1].lower()[:12] == 'byModifyTime'.lower():
                return SortByModifyTimeOption
            else:
                print('[Error] 不存在sort操作: ', option[1])
                sys.exit(0)

        elif option[0].lower() == '-maxSize'.lower():
            return MaxSizeOption

        elif option[0].lower() == '-minSize'.lower():
            return MinSizeOption

        elif option[0].lower() == '-include'.lower():
            return NameIncludeOption

        elif option[0].lower() == '-mode'.lower():
            if option[1].lower() == 'log'.lower():
                return LogModeOption
            elif option[1].lower() == 'diff'.lower():
                return DiffModeOption
            else:
                print('[Error] 不存在模式: ', option[1])
                sys.exit(0)

        elif option[0].lower() == '-calcDirSize'.lower():
            return CalcDirSizeOption

        else:
            print('[Error] 命令错误:', option[0], option[1])
            sys.exit(0)

