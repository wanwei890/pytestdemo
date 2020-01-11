#!/usr/bin/env python
# encoding: utf-8
"""
@author: wanwei
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: wei_wan@sui.com
@software: pycharm
@file: test_db.py
@time: 2019/9/24 13:46
@desc:
"""
from mytools.models import User
from mytools.extensions import db
from mytools import app


def test_password_hash(setup):
    """测试密码加密"""
    u = User(username="wanwei3")
    u.set_password("Huawei1234")
    assert u.check_password("Huawei1234") is True
    assert u.check_password("huwe") is False


def test_follow(setup_database):
    """测试关注函数"""
    with app.app_context():
        user1 = User.query.filter_by(username='wanwei').first()
        user2 = User.query.filter_by(username='wanwei2').first()
        assert user1.username == 'wanwei','user1 username不正确'
        assert user2.username == 'wanwei2','user2 username不正确'
