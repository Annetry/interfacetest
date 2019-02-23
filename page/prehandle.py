#coding:utf-8
import requests
import os

def getHeaders():
    '''获取请求头'''
    headers={"Parkingwang-Client-Source":"ParkingWangAPIClientWeb",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}
    return headers
def post(url,data):
    '''post请求二次封装，以后不用传headers和timeout'''
    r=requests.post(url=url,data=data,headers=getHeaders(),timeout=6)
    return r
def dir_base(filename,package='data'):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),package,filename)
