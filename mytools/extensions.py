#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project    : flask-mega-tutorial
# @Author     : Administrator
# @CreateTime : 2019/5/22 9:09
# @File       : extensions.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
