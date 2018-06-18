# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import re
from Option.Option import Option

class NameIncludeOption(Option):
    def __init__(self, pattern):
        super().__init__()
        self.pattern = re.compile(pattern, re.I)

    def execute(self, obj):
        return {
            key:value
            for key, value in obj.items()
            if len(self.pattern.findall(str(value['name'])))
        }
