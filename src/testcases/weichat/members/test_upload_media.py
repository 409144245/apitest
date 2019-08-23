#!/usr/bin/env python
# encoding: utf-8
from pages import media

class TestUploadMedie:

    def test_upload_medie(self):
        media_api = media.MediaAPI()
        res = media_api.upload_media()
        assert res.get('errcode') == 0

