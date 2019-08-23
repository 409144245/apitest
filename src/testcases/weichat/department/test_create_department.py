#!/usr/bin/env python
# encoding: utf-8
from pages import departmentnew
import os

class TestCreateDepartment:

    def test_create_department(self):
        print(os.path.basename(__file__))
        new_dep = departmentnew.DepartmentNew('../../../../cfg/testdata/test_create_department.json')
        json_dic = new_dep.create_department()
        assert json_dic.get('errmsg')=='created'
        assert json_dic.get('errcode')==0



