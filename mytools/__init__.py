import os

from flask import Flask
from mytools.logger import register_logger
from mytools.extensions import register_extensions


def create_app(test_config=None):
    """应用工厂函数"""
    app = Flask(__name__, instance_relative_config=True)

    # 加载config配置
    app.config.from_object('config')
    # testconfig：单独设置配置参数，替代实例配置，这样可以实现开发和测试环境分离，相互独立
    if test_config:
        app.config.from_mapping(test_config)
    # ---------注册Flask扩展库--------- #
    register_extensions(app)
    # ---------注册日志--------- #
    if not app.debug and not app.testing:
        register_logger(app)

    # ---------实例目录创建--------- #
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app

app = create_app()
from mytools import models


