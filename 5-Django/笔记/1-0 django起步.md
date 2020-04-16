1.0 django起步

1.0.1 Django简介
优点：简单，开发速度快，安全

1.0.2 安装Django（linux）
	安装指定版本：sudo pip install Django==1.10.1
	查看版本：import django
	                  print(django.get_version())
	源码安装：git clone https://github.com/django/django.git
		           sudo pip install -e ./django

1.0.3 创建项目(project)
	创建一个mysite项目：cd /data/mysite && django-admin startproject mysite
	或者：django-admin startppoject mysite .  （有__init__.py文件）
	启动项目：python manage.py runserver (可以通过http://127.0.0.1:8000/访问)
			  python3 manage.py runserver 0.0.0.0:8000（指定ip地址和端口）

1.0.4 项目的基本配置
	在Django 项目中，主管信息注册（对本项目进行各种信息声明〉的文件是./mysite/settings.py.
	BASE_DIR: os.path.dirname(os.path.dirname(os.path.abspath(file)))，这里BASE_DIR也就是整个工程project的目录，即djangotest这个目录
	DEBUG ：其值为True 或者False 。在开发过程中， 需要设置成True ，在测试功能时，Django 能够显示详细的报错信息一一这是"开发模式"。如果将项目部署到真正要对外发布的服务器上，我们称之为"生产环境",必须将其值修改为False ，从而避免暴露项目的内部信息。
	ALLOWED_HOSTS ：在DEBUG 为True 时，其值可以为空。当部署到生产环境中时，要把主域名填写到这里，才能通过域名访问到本网站。
	时STALLED_APPS ：这是一个非常重要的配置项，所有的应用只有写到这里才能生效。新增加的blog 'blog.apps.BlogConfig'
	DATABASES ：在这里可以配置数据库。
	LANGUAGE CODE ：设置项目的语言， 一般情况下可以不用修改.如果要使用汉语，则设置zh-hans
	TIME_ZONE ：设置时区，通常使用东八区，设置为“ Asia/Shanghai ”。
	STATIC_URL = '/static/'# 静态文件夹的别名
	STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
	]
	# 静态文件夹的位置
	
1.0.5 创建应用(application):用来隔离不同功能模块的代码
	python manage.py startapp blog ，应用创建后需要在settings.py文件中注册应用"'blog.apps.BlogConfig'"
	目录和文件说明：
	1. manage.py  在创建一个Django 项目后， manage.py被自动生成在项目的根目录中，它是对django-admin.py的简单封装，同样能够实现命令行操作。
	2. mysite mysite 是所建项目的管理功能目录，这个目录的名称因用户所创建的项目名称的不同而异.
		1) settings.py：这个文件中包括了项目的初始化设置，可以针对整个项目进行有关参数配置，比如配置数据库、添加应用等。
		2) urls.py：这是一个URL 配置表文件，主要是将URL 映射到应用程序上。当用户请求某个url时， Django 项目会根据这个文件中的映射关系指向某个目标对象，该对象可以是某个应用中的urls.py 文件，也可以是某个具体的视图函数。在Django 中，这个文件也被称为URLconf.
		3) wsgi.py: WSGI 是Web Server Gateway Interface 的缩写
	3. blog 是在项目中所创建的应用之一，注意是之一，用创建应用的指令还可以创建很多其他的应用。
		1) admin.py：在这个文件中，可以自定义Django 管理工具，比如设置在管理界面能够管理的项目，或者通过重新自定义与系统管理有关的类对象，向管理功能增加新的内容。
		2) apps.py：这个文件是眨jangol.10 之后增加的，通常包含对应用的配置，比如为管理功能提供一个适合的应用名称。
		3) migrations：这是一个目录，用于存储应用的数据库表结构的指令，通过这些指令可以修改和创建数据库，从而在models.py 模型类和数据库表之间迁移。
		4) models.py：这是应用的数据模型，每个问ango 应用都应当有一个models.py 文件.		        			           
                 5) views.py   这是一个重要的文件，用户保存响应各种请求的函数或者类。如果编写的是函数，则称之为基于函数的视图：如果编写的是类，则称之为基于类的视图。views.py就是保存函数或者类的视图文件。
	4. templates 存放静态的HTML文件,告诉Django去哪儿找我的HTML文件
	5. static 存放js,css等文件
	6. db.sqlite3 默认的数据库 

1.0.6 知识点
	1. 开发模式：没有正式对外部客户提供服务，这种模式下很多配置都是为了开发而定的，比如在Djang开发模式中， 不需要配置A pache 或者Nginx 等服务器，也能够运行网站，这是因为Django 本身就提供了简单的Web 服务器功能。
	在开发模式中， Django 会自动检测到修改的代码并重新加载，不需要每次修改代码后重新启动Web 服务器。只有在新增加文件后，才需要重启Django 服务。运行Django服务的指令是python manage.py runserver.
	Django 安装好之后，就有了django-admin 这个默认命令，可以用diango-admin startprproject projectname 命令创建一个Django 项目。项目是由若干个“应用(app) 组成的， 实现具体功能。创建应用可以使用python manag.py startapp appname 命令，也可以使用django-amdin startapp appname 命令。每个应用都要在项目的settings.py 丈件的INSTALLED_APPS 中进行声明，告诉Djang 。这个应用是本项目的一部分。
	2. GET请求和POST请求
		GET请求:
			1. 浏览器请求一个页面
			2. 搜索引擎检索关键字的时候
			
		POST请求:
			1. 浏览器向服务端提交数据,比如登录/注册等
