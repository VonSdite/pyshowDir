# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import sys
from Option.Option import Option

class SortOption(Option):

    def __init__(self, order):
        super().__init__()
        self.order = order

    def execute(self, obj):
        pass

class SortByNameOption(SortOption):

    def __init__(self, order):
        super().__init__(order)

    def execute(self, obj):
        order = self.order[6:]
        if order.lower() == 'asc':
            return dict(
                sorted(
                obj.items(),
                key=lambda x: x[1]['name']
                )
            )
        elif order.lower() == 'dec':
            return dict(
                sorted(
                obj.items(),
                key=lambda x: x[1]['name'],
                reverse=True
                )
            )
        else:
            print('[Error] 不存在排序规则:', self.order)
            sys.exit(0)


class SortBySizeOption(SortOption):

    def __init__(self, order):
        super().__init__(order)

    def execute(self, obj):
        order = self.order[6:]
        if order.lower() == 'asc':
            return dict(
                sorted(
                obj.items(),
                key=lambda x: x[1]['size']
                )
            )
        elif order.lower() == 'dec':
            return dict(
                sorted(
                obj.items(),
                key=lambda x: x[1]['size'],
                reverse=True
                )
            )
        else:
            print('[Error] 不存在排序规则:', self.order)
            sys.exit(0)

class SortByModifyTimeOption(SortOption):

    def __init__(self, order):
        super().__init__(order)

    def execute(self, obj):
        order = self.order[12:]
        if order.lower() == 'asc':
            return dict(
                sorted(
                obj.items(),
                key=lambda x: x[1]['modifyTime']
                )
            )
        elif order.lower() == 'dec':
            return dict(
                sorted(
                obj.items(),
                key=lambda x: x[1]['modifyTime'],
                reverse=True
                )
            )
        else:
            print('[Error] 不存在排序规则:', self.order)
            sys.exit(0)