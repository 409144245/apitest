#!/usr/bin/env python
# encoding: utf-8

from pages.gettoken import GetTokenAPI
import requests
import codecs

class DepartmentNew(GetTokenAPI):

    def __init__(self,json_file):
        self.corp_secret='kvKsV96fn-G9M5U50l36XKgbPp2NVj6MemxQRa3-nPg'
        GetTokenAPI.__init__(self,self.corp_secret)
        self.json_file = json_file
        self.create_url='https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token='

    def read_json_file(self):
        json_fi = codecs.open(self.json_file,'r',encoding='utf-8')
        json_content = json_fi.read()
        json_fi.close()
        return json_content.encode('utf-8')

    def create_department(self):
        token = self.get_token()
        json_content ='{"name": "运营部","parentid": 1,"order": 1,"id": 7}'.encode('utf-8')
        res = requests.post(self.create_url+token, data=json_content)
        return res.json()



