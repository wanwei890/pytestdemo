#!/usr/bin/env python
# encoding: utf-8
"""
@author: wanwei
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@software: pycharm
@file: logger.py
@time: 2019/7/24 16:47
@desc:
"""

import os
import logging
from logging.handlers import RotatingFileHandler


def register_logger(app):
    # 创建log目录，用于存放日志文件
    if not os.path.exists('./mytools/logs'):
        os.mkdir('./mytools/logs')

    # 设置RotatingFileHandler，最大日志文件100k，备份10个
    file_hander = RotatingFileHandler('./mytools/logs/assistant.log', maxBytes=102400, backupCount=10, encoding='utf8')
    # logging.Formatter类为日志消息提供自定义格式
    # 分别记录了时间戳、日志记录级别、消息、日志来源的源代码文件和行号
    file_hander.setFormatter(logging.Formatter(
        '%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s: %(message)s '
    ))

    # 设置日志类别：分别是DEBUG、INFO、WARNING、ERROR和CRITICAL
    file_hander.setLevel(logging.INFO)
    app.logger.addHandler(file_hander)

    # 每次服务重新启动，都会登记一条日志
    app.logger.setLevel(logging.INFO)
    app.logger.info("datatestdemo 已启动..........................")
