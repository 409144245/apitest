#!/usr/bin/env python
# encoding: utf-8
import allure
import pytest
from pages import gettoken

allure.feature('测试审批功能')
class TestApprovalByPO:
    get_token_interface = gettoken.GetTokenAPI('TJUU19T_yG_83tJQlXU8P3Fg37VCV2eTo8e574RUivc')
    get_wrong_token_interface = gettoken.GetTokenAPI('222')

    @allure.story('输入正确的securetID获取到access token')
    def test_get_access_token(self):
        res = TestApprovalByPO.get_token_interface.get_token_res_by_subpath()
        assert 'access_token' in res.keys()

    @allure.story('通过request传入parameters的方式获取到access token')
    def test_get_access_token_by_parameters(self):
        res = TestApprovalByPO.get_token_interface.get_token_by_parameters()
        pytest.assume('access_token' in res.keys())
        pytest.assume(res.get('errcode')==0)

    @allure.story('通过request传入parameters的方式获取到access token')
    def test_get_access_token_by_parameters(self):
        res = TestApprovalByPO.get_token_interface.get_token_res_by_parameters()
        pytest.assume('access_token' in res.keys())
        pytest.assume(res.get('errcode') == 0)

    @allure.story('传入错误的corpsecret获取不到access_token')
    def test_no_get_access_token(self):
        res = TestApprovalByPO.get_wrong_token_interface.get_token_res_by_parameters()
        pytest.assume('access_token' not in res.keys())
        pytest.assume(res.get('errcode') == 40001)

