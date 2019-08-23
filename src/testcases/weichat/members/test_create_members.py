#!/usr/bin/env python
# encoding: utf-8

from pages import members

class TestCreateMembers:

    def test_create_members(self):
        members_api = members.MembersAPI('../../../../cfg/testdata/test_create_members.json')
        res = members_api.create_member()
        assert res.get('errmsg') == 'created'

