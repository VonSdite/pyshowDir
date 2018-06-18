# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import sys
from Option.Option import Option

def parseSize(size):
    try:
        if size[-2] not in '0123456789':
            if size[-2:].lower() == 'KB'.lower():
                return float(size[:-2]) * 1024
            elif size[-2:].lower() == 'MB'.lower():
                return float(size[:-2]) * 1024 * 1024
            elif size[-2:].lower() == 'GB'.lower():
                return float(size[:-2]) * 1024 * 1024 * 1024
            else:
                print('[Error] 没有单位:', size[-2:])
                sys.exit(0)
        else:
            if size[-1].lower() == 'B'.lower():
                return float(size[:-1])
            elif size[-1] in '0123456789':
                print('[Error] 缺少单位')
                sys.exit(0)
            else:
                print('[Error] 没有单位:', size[-1:])
                sys.exit(0)
    except:
        print('[Error] 错误大小:', size)
        sys.exit(0)

class SizeOption(Option):

    def __init__(self, size):
        super().__init__()
        self.size = parseSize(size)

    def execute(self, obj):
        pass

class MaxSizeOption(SizeOption):
    def __init__(self, size):
        super().__init__(size)

    def execute(self, obj):
        if isinstance(self.size, float):
            return {
                key:value
                for key, value in obj.items()
                if float(value['size']) <= self.size
            }
        else:
            print('[Error] 错误大小:', self.size)
            sys.exit(0)

class MinSizeOption(SizeOption):
    def __init__(self, size):
        super().__init__(size)

    def execute(self, obj):
        if isinstance(self.size, float):
            return {
                key: value
                for key, value in obj.items()
                if float(value['size']) >= self.size
            }
        else:
            print('[Error] 错误大小:', self.size)
            sys.exit(0)
