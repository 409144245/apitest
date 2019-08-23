#!/usr/bin/env python
# encoding: utf-8

import logging
import os
import requests
from .gettoken import GetTokenAPI
import codecs

class DepartmentAPI(GetTokenAPI):
    def __init__(self, json_file):
        self.corpsecret = 'kvKsV96fn-G9M5U50l36XKgbPp2NVj6MemxQRa3-nPg'
        GetTokenAPI.__init__(self, self.corpsecret)
        self.json_file = json_file
        self.creat_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token='
        self.list_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token='

    def read_json_file(self):
        if os.path.exists(self.json_file):
            json_str = codecs.open(self.json_file,'r',encoding='utf-8')
            json_content = json_str.read().strip()
            json_str.close()
            return json_content.encode('utf-8')
        else:
            print(self.json_file + ' not exist')

    def create_department(self):
        print(self.read_json_file())
        access_token = self.get_token()
        #data='{"name": "销售部","parentid": 1,"order": 1,"id": 4}'
        #res = requests.post(self.url+access_token, data = data.encode('utf-8'))
        res = requests.post(self.creat_url + access_token, data=self.read_json_file())

        return res.json()





