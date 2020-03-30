#!/usr/bin/env python
# encoding: utf-8
"""
@author: wanwei
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@software: pycharm
@file: pytest1.py
@time: 2019/9/29 15:29
@desc:
"""
import pytest


@pytest.mark.recommend
def test_1(setup_function):
    print("test_1 called...")


def test_2(setup_test):
    # assert 1 != 1
    print("test_2 called...")


def test_3(setup_test):
    print("test_3 called...")
