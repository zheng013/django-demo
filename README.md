```(lua)
——mysite        --代表整个程序的配置目录
  init        --默认需要生成的文件，代表这个目录是一个模块
  settings    --项目的配置文件
  url         --URL对应路由界面的关系
  wsgi        --遵循的规范 uwsgi+nginx
manage.py     --命令行执行的工具，可以使用多种方式对项目进行交互

```

# python -m django --version

# django-admin.py startproject mysite

# python manage.py runserver

# python manage.py startapp blog

```(lua)
 admin.py       --对应应用的后台管理配置文件
 apps.py        --对应应用的配置文件
 models.py      --数据模块   涉及关于数据库的设计模块
 tests.py       --自动化测试模块   可编写测试脚本自动化测试
 views.py       --视图文件  用于执行响应代码

migrations      --数据迁移、移植目录文件 记录数据库操作记录，内容和表自动生成。

```

## 关于django常用的一些命令
```(lua)
安装Django  pip install django==[指定版本]
新建项目     django-admin.py startproject mysite
新建App     python manage.py startapp blog
启动        python manage.py runserver 8080

同步或者更改生成 数据库
            python  manage.py  makemigrations
            python  manage.py  migrate

清空数据库    python  manage.py  flush
创建管理员    python  manage.py  createsuperuser
修改用户密码   python  manage.py  changepassword username
Django项目环境终端  python  manage.py  shell

```