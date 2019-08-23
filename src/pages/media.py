#!/usr/bin/env python
# encoding: utf-8

import requests
from .gettoken import GetTokenAPI
import codecs

class MediaAPI(GetTokenAPI):
    def __init__(self):
        self.corpsecret = 'kvKsV96fn-G9M5U50l36XKgbPp2NVj6MemxQRa3-nPg'
        GetTokenAPI.__init__(self, self.corpsecret)
        self.upload_url = 'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token='
        self.res_json = ''

    def upload_media(self):
        access_token = self.get_token()
        print(access_token)
        files =  {'media': ('th.jpg',open('th.jpg','rb'),'image/jpg')}
        #data='{"name": "销售部","parentid": 1,"order": 1,"id": 4}'
        res = requests.post(self.upload_url + access_token+'&type=file', files=files)
        self.res_json = res.json()
        print('media_id:'+self.res_json.get('media_id'))
        return self.res_json

    def get_medie_id(self):
        if 'media_id' in self.self.res_json.keys():
            return self.res_json.get('media_id')
        else:
            return False