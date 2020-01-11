# 接口测试&单元测试

## 本地开发环境部署
1. git clone 或者 checkout至本地目录
2. 修改：MockServer/config.py 数据库相关配置
    ```python
    USERNAME = 'root'
    PASSWORD = '123456'
    HOST = '127.0.0.1'
    DB = 'mockservertest'
    ```
3. 安装相应依赖库
    ```bash
    pip install -r requirements.txt
    ```
4. 创建datatest数据库, 默认DB是datatest
    CREATE DATABASE IF NOT EXISTS datatest DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
5. 生成数据库迁移脚本，应用表结构
    ```bash
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    ```
6. 打开cmd，进入datatestdemo目录，按以下方式即可运行测试用例：
- pytest #运行所有用例，结果以"."方式输出，不打印用例运行详细结果
- pytest -v #输出用例运行列表
- pytest s #打印输出print函数，pytest -v