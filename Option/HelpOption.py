# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

from Option.Option import Option

class HelpOption(Option):
    def __init__(self):
        super().__init__()

    def execute(self):
        helpDoc = '''
用法: showDir.py path [-mode mode] [-sort order] 
                [-include str] [-maxSize size] [-minSize size]
                [-calcDirSize bool] [-help]
                
      showDir.exe path [-mode mode] [-sort order] 
                [-include str] [-maxSize size] [-minSize size]
                [-calcDirSize bool] [-help]
                
选项:
    -mode mode          选择程序进入的模式。
                        mode在[log, diff]中取，且该选项不能与其它选项一起用
                        -mode log  表示日志模式
                        -mode diff 表示差异模式，需先运行日志模式
        
    -sort order         对查询的结果排序。
                        order在[byNameAsc, byNameDec, bySizeAsc, bySizeDec,
                        byModifyTimeAsc, byModifyTimeDec]中取，能与其它选项一起使用
                        -sort byNameAsc         表示按文件名升序排序
                        -sort byNameDec         表示按文件名降序排序
                        -sort bySizeAsc         表示按文件大小升序排序
                        -sort bySizeDec         表示按文件大小降序排序
                        -sort byModifyTimeAsc   表示按修改时间升序排序
                        -sort byModifyTimeDec   表示按修改时间降序排序
        
    -include str        筛选包含str的文件(目录)名
                        str参数为正则表达式语法(语法同python正则表达式)
            
    -maxSize size       筛选文件(目录)大小 <=size的文件 
                        (目录大小需使用选项 -calcDirSize true)
        
    -minSize size       筛选文件(目录)大小 >=size的文件 
                        (目录大小需使用选项 -calcDirSize true)   
                    
    -calcDirSize bool   是否计算目录的大小        
                        bool在[true, false]中取值
                        -calcDirSize true       表示要计算目录大小
                        -calcDirSize false      表示不要计算目录大小
                        
    -help               查看帮助
'''
        print(helpDoc)
