#!/usr/bin/env python
# encoding: utf-8

import requests
from .media import MediaAPI
import codecs
import os

class MembersAPI(MediaAPI):
    def __init__(self,json_file):
        self.json_file = json_file
        self.corpsecret = 'kvKsV96fn-G9M5U50l36XKgbPp2NVj6MemxQRa3-nPg'
        MediaAPI.__init__(self)
        self.create_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token='

    def read_json_file(self):
        if os.path.exists(self.json_file):
            json_str = codecs.open(self.json_file,'r',encoding='utf-8')
            json_content = json_str.read().strip()
            json_str.close()
            return json_content.encode('utf-8')
        else:
            print(self.json_file + ' not exist')

    def create_member(self):
        access_token = self.get_token()
        print('accss_token:'+access_token)
        res = requests.post(self.create_url + access_token, data=self.read_json_file())
        return res.json()
