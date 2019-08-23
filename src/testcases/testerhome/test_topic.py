#!/usr/bin/env python
# encoding: utf-8
#author: Jim Yin

import allure
import requests


@allure.feature('通过api接口获取topic')
class TestTopic:

    def test_maxlike_topic(self):
        topic_res = requests.get('https://testerhome.com/api/v3/topics.json')
        print(topic_res.json())