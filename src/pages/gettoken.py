#!/usr/bin/env python
# encoding: utf-8
import logging
import requests

class GetTokenAPI:

    def __init__(self, corpsecret):
        logging.info('init the get token api interface')
        self.token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        self.corpid='ww4dfe3ca234f977f6'
        self.corpsecret=corpsecret

    #requests.get(url)
    def get_token_res_by_subpath(self):
        logging.info('get token by sub path')
        res = requests.get(self.token_url+'?'+'corpid='+self.corpid+'&corpsecret='+self.corpsecret)
        return res.json()

    #requests.get(url, params = payload)
    def get_token_res_by_parameters(self):
        logging.info('get token by parameters')
        payload = {'corpid': self.corpid, 'corpsecret': self.corpsecret}
        res = requests.get(self.token_url, params = payload)
        print('headers:'+str(res.headers))
        print('text:' + str(res.text))
        return res.json()

    def get_token(self):
        if 'access_token' in self.get_token_res_by_parameters():
            return self.get_token_res_by_parameters().get('access_token')
        else:
            return False







