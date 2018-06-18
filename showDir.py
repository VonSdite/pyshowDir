# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import sys
from App.OodleApp import OodleApp

if __name__ == '__main__':
    queryPath = sys.argv[1:2][0] if len(sys.argv[1:2]) else ''
    option = sys.argv[2:]
    app = OodleApp(queryPath, option)
