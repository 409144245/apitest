#!/usr/bin/env python
# encoding: utf-8
#author: Jim Yin
import pytest
import logging

fileHandler=logging.FileHandler(filename='../log/apiauto.log',encoding='utf8')
logging.getLogger().setLevel(0)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
fileHandler.setFormatter(formatter)

if __name__=='__main__':
    pass


