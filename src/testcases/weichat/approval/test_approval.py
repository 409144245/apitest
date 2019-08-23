#!/usr/bin/env python
# encoding: utf-8
import logging
import allure
import requests
import pytest
import json

allure.feature('测试审批功能')
class TestApproval:

    @allure.story('输入正确的securetID获取到access token')
    def test_get_access_token(self):
        res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww4dfe3ca234f977f6&corpsecret=TJUU19T_yG_83tJQlXU8P3Fg37VCV2eTo8e574RUivc')
        assert 'access_token' in res.json().keys()

    @allure.story('通过request传入parameters的方式获取到access token')
    def test_get_access_token_by_parameters(self):
        payload = {'corpid':'ww4dfe3ca234f977f6','corpsecret':'TJUU19T_yG_83tJQlXU8P3Fg37VCV2eTo8e574RUivc'}
        res = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',params = payload)
        pytest.assume('access_token' in res.json().keys())
        pytest.assume(res.json().get('errcode')==0)

