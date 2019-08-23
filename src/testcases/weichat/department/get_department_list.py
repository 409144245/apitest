#!/usr/bin/env python
# encoding: utf-8


import logging
from pages import department

class TestGetDepList:

    def test_get_department(self):
        logging.info('test to get new department')

        dep_api = department.DepartmentAPI('../../../../cfg/testdata/test_create_new_department.json')
        create_res = dep_api.create_department()
        assert create_res.get('errmsg')== 'created'
        assert create_res.get('errcode') == 0






