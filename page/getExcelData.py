#coding:utf-8
import xlrd
from wuya.page.prehandle import *
import os
import json
class getEdata(object):
    def readExcel(self,rowx,sheet=0):
        '''读取excel文件数据'''
        epath=os.path.join(dir_base('postdata.xlsx'))
        excelsheet=xlrd.open_workbook(epath)
        table=excelsheet.sheet_by_index(sheet)
        return table.row_values(rowx)
    def readurl(self,rowx):
        '''读取第rowx行第1列数据'''
        return self.readExcel(rowx)[1]
    def readdata(self,rowx):
        '''读取第rowx行第2列数据'''
        return json.loads(self.readExcel(rowx)[2])

