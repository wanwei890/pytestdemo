#!/usr/bin/env python
# encoding: utf-8
"""
@author: wanwei
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@software: pycharm
@file: conftest.py
@time: 2019/9/24 11:02
@desc:
"""
import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from mytools import create_app
from mytools.extensions import db

# 加载数据初始化SQL语句文件
with open(os.path.join(os.path.dirname(__file__), './data/setup.sql'), 'rb') as f:
    _setup_sql = f.readlines()

# 销毁数据SQL语句文件
with open(os.path.join(os.path.dirname(__file__), './data/teardown.sql'), 'rb') as f:
    _teardown_sql = f.readlines()


@pytest.fixture(scope='session')
def setup(request):
    def teardown():
        print("用例执行结束..................................")
    request.addfinalizer(teardown)
    print("用例执行开始..................................")

@pytest.fixture(scope="module")
def setup_database(request):
    print("setup tb_user开始执行...............")
    # ----------FLASK-SQLALCHEMY数据库配置---------#
    USERNAME = 'root'
    PASSWORD = '123456'
    HOST = '127.0.0.1'
    DB = 'datatest'

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://%s:%s@%s/%s' % (USERNAME, PASSWORD, HOST, DB)
    # 创建应用实例
    app = create_app({
        'TESTING': True,
        # 数据库文件存放路径
        'SQLALCHEMY_DATABASE_URI': SQLALCHEMY_DATABASE_URI,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_ECHO': False
    })
    def teardown_database():
        print("teardown tb_user开始执行...............")
        with app.app_context():
            #初始化数据库模型
            db.create_all()
            for sql in _teardown_sql:
                if sql:
                    db.engine.execute(sql.decode('utf-8'))
    request.addfinalizer(teardown_database)
    with app.app_context():
        for sql in _setup_sql:
            if sql:
                db.engine.execute(sql.decode('utf-8'))


@pytest.fixture(scope='function')
def setup_function(request):
    def teardown_function():
        print("teardown_function called...")
    request.addfinalizer(teardown_function)  # 内嵌函数做teardown操作
    print("setup_function called...")


@pytest.fixture(scope='module')
def setup_test(request):
    def teardown_test():
        print("teardown_module called...")
    request.addfinalizer(teardown_test)
    print("setup_module called...")
