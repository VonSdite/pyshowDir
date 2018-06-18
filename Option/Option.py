# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com


class Option(object):
    def __init__(self):
        super().__init__()

    def execute(self, obj):
        pass

class Options(Option):

    def __init__(self):
        super().__init__()

        self.optionList = []

    def addOption(self, option):
        self.optionList.append(option)

    def execute(self, obj):
        for option in self.optionList:
            obj = option.execute(obj)

        return obj