#coding:utf-8
import json
import unittest
from wuya.page.getExcelData import getEdata
from wuya.page.prehandle import *
class UserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    def getUrl(self,rowx):
        return getEdata().readurl(rowx)
    def getData(self,rowx):
        return getEdata().readdata(rowx)

    def test_login(self):
        '''使用表格第1行的数据请求'''
        s=requests.session()
        res=s.post(self.getUrl(0),self.getData(0))
        with open(dir_base('token.txt'),'w') as f:
            f.write(json.loads(res)['data']['token'])

    def getToken(self):
        '''获取token'''
        with open(dir_base('token.txt'),'r') as f:
            return f.read()

    def setToken(self,rowx):
        '''对列表data中的token重新赋值'''
        dict1=self.getData(rowx)
        dict1['token']=self.getToken()
        return dict1

    def statusCode(self,res):
        self.assertEqual(res.status_code,200)
        '''业务状态码'''
        self.assertEqual(res.json()['status'],0)

    def test_user_002(self):
        '''使用表格数据，重新得到的token请求'''
        r=post(self.getUrl(2),self.setToken(2))
        self.statusCode(r)
        self.assertEqual(r.json['data']['expire'],False)

    def test_user_003(self):
        r = post(self.getUrl(3), self.setToken(3))
        with open(dir_base('userid','data'),'w') as f:
            f.write(r.json()['data']['id'])
    def getUserId(self):
        with open(dir_base('userid','data'),'w') as f:
            return int(f.read())
    def setTokenUserId(self,rowx):
        dict2=self.getData(rowx)
        dict2['token']=self.getToken()
        dict2['id']=self.getUserId()

