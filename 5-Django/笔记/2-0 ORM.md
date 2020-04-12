2.0 对象关系映射（Object Relational Mapping，简称ORM）

2.0.1 ORM介绍
1 ORM概念
对象关系映射（Object Relational Mapping，简称ORM）模式是一种为了解决面向对象与关系数据库存在的互不匹配的现象的技术。
简单的说，ORM是通过使用描述对象和数据库之间映射的元数据，将程序中的对象自动持久化到关系数据库中。
ORM在业务逻辑层和数据库层之间充当了桥梁的作用。

2 ORM特点
ORM提供了对数据库的映射，不用直接编写SQL代码，只需像操作对象一样从数据库操作数据。让软件开发人员专注于业务逻辑的处理，提高了开发效率。
ORM的缺点是会在一定程度上牺牲程序的执行效率。

3 ORM的对应关系:
		类          --->      数据表
		对象        --->      数据行
		属性        --->      字段
		
2.0.2 使用Django的ORM详细步骤:
	1. 自己动手创建数据库
		create database 数据库名;
	2. 在Django项目中设置连接数据库的相关配置(告诉Django连接哪一个数据库)
		# 数据库相关的配置
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.mysql',  # 连接的数据库类型
				'HOST': '127.0.0.1',  # 连接数据库的地址
				'PORT': 3306,  # 端口
				'NAME': "day61",  # 数据库名称
				'USER': 'root',  # 用户
				'PASSWORD': '123456'  # 密码
			}
		}
	3. 告诉Django用pymysql代替默认的MySQLDB 连接MySQL数据库
		在项目/__init__.py文件中,写下面两句:
			import pymysql
			# 告诉Django用pymysql来代替默认的MySQLdb
			pymysql.install_as_MySQLdb()
	4. 在app下面的models.py文件中定义一个类,这个类必须继承models.Model
		class 类名(models.Model):
			...
	5. 执行两个命令
		1. python3 manage.py makemigrations #把models.py文件中的变动记录到migration文件中
		2. python3 manage.py migrate		#自动翻译为SQL语句去执行
		
2.0.3 快速入门小例子 
	1.定义了一个 Person 模型，包含 first_name 和 last_name。
	from django.db import models

	class Person(models.Model):
		first_name = models.CharField(max_length=30)
		last_name = models.CharField(max_length=30)
	first_name 和 last_name 是模型的字段。每个字段被指定为一个类属性，每个属性映射到一个数据库列。

	上面的 Person 模型将会像这样创建一个数据库表：

	CREATE TABLE myapp_person (
		"id" serial NOT NULL PRIMARY KEY,
		"first_name" varchar(30) NOT NULL,
		"last_name" varchar(30) NOT NULL
	);
	一些说明：
	表myapp_person的名称是自动生成的，如果你要自定义表名，需要在model的Meta类中指定 db_table 参数，强烈建议使用小写表名，特别是使用MySQL作为后端数据库时。
	id字段是自动添加的，如果你想要指定自定义主键，只需在其中一个字段中指定 primary_key=True 即可。如果Django发现你已经明确地设置了Field.primary_key，它将不会添加自动ID列。
	本示例中的CREATE TABLE SQL使用PostgreSQL语法进行格式化，但值得注意的是，Django会根据配置文件中指定的数据库后端类型来生成相应的SQL语句。		

	2.删除表 注释掉application下面的models.py中的对应的class，然后执行两个命令
	3.修改表 修改掉application下面的models.py中的对应的字段，然后执行两个命令
	
	
		
		
		
