2.1.1 ORM 常用字段和参数
	1、AutoField	
		id = models.AutoField(primary_key=True) # 创建一个自增的主键字段
		int自增列，必须填入参数 primary_key=True。当model中如果没有自增列，则自动会创建一个列名为id的列。
	2、CharField	
		name = models.CharField(null=False, max_length=32) # 创建一个varchar(20)类型的不能为空的字段
		字符类型，必须提供max_length参数， max_length表示字符长度。
		null:布尔值，用于表示某个字段是否可以为空。 
		unique：布尔值，用于表示该字段在此表中必须是唯一的。
	3、IntegerField：一个整数类型,范围在 -2147483648 to 2147483647。
	4、DateField： 日期字段，日期格式  YYYY-MM-DD，相当于Python中的datetime.date()实例。
	5、DateTimeField：日期时间字段，格式 YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]，相当于Python中的datetime.datetime()实例。
		DatetimeField、DateField、TimeField这个三个时间字段，都可以设置如下属性。
		auto_now_add：配置auto_now_add=True，创建数据记录的时候会把当前时间添加到数据库。
		auto_now：配置上auto_now=True，每次更新数据记录的时候会更新该字段。
	6、DecimalField: 一个固定精度的十进制数类型，使用时必须要传递两个参数，max_digits数字的最大总长度(不含小数点),decimal_places小数部分的长度	
2.1.2 字段参数
	null：用于表示某个字段可以为空。
	unique;如果设置为unique=True 则该字段在此表中必须是唯一的 。
	db_index:如果db_index=True 则代表着为此字段设置数据库索引。
	default:为该字段设置默认值。
	
2.1.3 关系字段,一对多
	1、ForeignKey
		外键类型在ORM中用来表示外键关联关系，一般把ForeignKey字段设置在 '一对多'中'多'的一方。
		ForeignKey可以和其他表做关联关系同时也可以和自身做关联关系。
		字段参数
			to 设置要关联的表，表引号
			to_field 设置要关联的表的字段
			related_name 反向操作时，使用的字段名，用于代替原反向查询时的'表名_set'。
			on_delete:当删除关联表中的数据时，当前表与其关联的行的行为。
				models.CASCADE:删除关联数据，与之关联也删除
			db_constraint:是否在数据库中创建外键约束，默认为True。
			例如：
				class Classes(models.Model):
					name = models.CharField(max_length=32)				
				class Student(models.Model):
					name = models.CharField(max_length=32)
					theclass = models.ForeignKey(to="Classes")
		正向查询：通过学生来查找班级
			ret = models.Student..objects.all() 
			ret[0].theclass.name #theclass其实是一个指向Classes的对象，并不是一个属性值，theclass_id才是一个具体的值，数据库中表的字段就是theclass_id。
	2、ForeignKey操作
		1)、正向查找：
			对象查找（跨表）
				语法：对象.关联字段.字段
				示例：
					book_obj = models.Book.objects.first()  # 第一本书对象
					print(book_obj.publisher)  # 得到这本书关联的出版社对象
					print(book_obj.publisher.name)  # 得到出版社对象的名称
			字段查找（跨表）
			语法：关联字段__字段
				示例：
					print(models.Book.objects.values_list("publisher__name"))
		2)、反向操作
			对象查找
				语法：obj.表名_set
				示例：
					publisher_obj = models.Publisher.objects.first()  # 找到第一个出版社对象
					books = publisher_obj.book_set.all()  # 找到第一个出版社出版的所有书，<QuerySet [<Books: Books object>]>
					titles = books.values_list("title")  # 找到第一个出版社出版的所有书的书名
			字段查找
				语法：表名__字段
					示例：
					titles = models.Publisher.objects.values_list("book__title")
2.1.4 关系字段,多对多					
	1、ManyToManyField：多对多关联关系，将会创建出第三张表来说明对应关系
		class Author(models.Model):
			id = models.AutoField(primary_key=True)
			name = models.CharField(max_length=16, null=False, unique=True)
			book = models.ManyToManyField(to="Book") 
			# 将会生成第三张表author_book
			# author_obj = models.Author.objects.get(id=1)
			# author_obj.book 返回的为app01.Books.None，ORM封装的一个管理对象
			# author_obj.book.all() 返回的为<QuerySet [<Books: Books object>, <Books: Books object>]>
			# 在前端HTML中可以写author_obj.book.all，同时在for循环中直接使用变量author_obj.book.all，{% for book in author.book.all %}
	2、方法
		create() 创建一个新的对象，保存对象，并将它添加到关联对象集之中，返回新创建的对象。
			通过作者创建一本书,会自动保存
	        做了两件事：
		    1. 在book表里面创建一本新书，2. 在作者和书的关系表中添加关联记录
            author_obj.books.create(title="金老板自传", publisher_id=2)
		add() 把指定的model对象添加到关联对象集中。
			book_obj = models.Book.objects.get(id=4)
            author_obj.books.add(book_obj)
            添加多个
            book_objs = models.Book.objects.filter(id__gt=5)
            author_obj.books.add(*book_objs)  # 要把列表打散再传进去
            直接添加id
            author_obj.books.add(9)
		set() 更新model对象的关联对象。
		remove() 从关联对象集中移除执行的model对象
			book_obj = models.Book.objects.get(title="跟金老板学开飞船")
			author_obj.books.remove(book_obj)
			直接删除id
			author_obj.books.remove(8)
		clear() 从关联对象集中移除一切对象。	
			jing_obj = models.Author.objects.get(id=2)	
			jing_obj.books.clear()
	3、多对多关联关系的三种方式
		1）方式一：自行创建第三张表
			class Book(models.Model):
				title = models.CharField(max_length=32, verbose_name="书名")
			class Author(models.Model):
				name = models.CharField(max_length=32, verbose_name="作者姓名")		
			# 自己创建第三张表，分别通过外键关联书和作者
			class Author2Book(models.Model):
				author = models.ForeignKey(to="Author")
				book = models.ForeignKey(to="Book")
				
				class Meta:
					unique_together = ("author", "book")
		2）方式二：通过ManyToManyField自动创建第三张表
			class Book(models.Model):
				title = models.CharField(max_length=32, verbose_name="书名")			
			# 通过ORM自带的ManyToManyField自动创建第三张表
			class Author(models.Model):
				name = models.CharField(max_length=32, verbose_name="作者姓名")
				books = models.ManyToManyField(to="Book", related_name="authors")
		3）方式三：设置ManyTomanyField并指定自行创建的第三张表
			class Book(models.Model):
				title = models.CharField(max_length=32, verbose_name="书名")			
			# 自己创建第三张表，并通过ManyToManyField指定关联
			class Author(models.Model):
				name = models.CharField(max_length=32, verbose_name="作者姓名")
				books = models.ManyToManyField(to="Book", through="Author2Book", through_fields=("author", "book"))
				# through_fields接受一个2元组（'field1'，'field2'）：
				# 其中field1是定义ManyToManyField的模型外键的名（author），field2是关联目标模型（book）的外键名。						
			class Author2Book(models.Model):
				author = models.ForeignKey(to="Author")
				book = models.ForeignKey(to="Book")
				
				class Meta:
					unique_together = ("author", "book")
					
		注意：
			当我们需要在第三张关系表中存储额外的字段时，就要使用第三种方式。
			但是当我们使用第三种方式创建多对多关联关系时，就无法使用set、add、remove、clear方法来管理多对多的关系了，需要通过第三张表的model来管理多对多关系
2.1.5 关系字段,一对一	
	1、OneToOneField：一对一字段。通常一对一字段用来扩展已有字段。一对一的关联关系多用在当一张表的不同字段查询频次差距过大的情况下，将本可以存储在一张表的字段拆开放置在两张表中，然后将两张表建立一对一的关联关系。如一张作者表，另外一张作者详情表。
	字段参数：to
	设置要关联的表：to_field
	设置要关联的字段：on_delete（同ForeignKey字段）
	
2.1.6 聚合查询和分组查询
	1、聚合
		aggregate()是QuerySet 的一个终止子句，意思是说，它返回一个包含一些键值对的字典。
		键的名称是聚合值的标识符，值是计算出来的聚合值。键的名称是按照字段和聚合函数的名称自动生成出来的。
		用到的内置函数：
		from django.db.models import Avg, Sum, Max, Min, Count
		示例：
			>>> from django.db.models import Avg, Sum, Max, Min, Count
			>>> models.Book.objects.all().aggregate(Avg("price"))
			{'price__avg': 13.233333}
			
			如果你想要为聚合值指定一个名称，可以向聚合子句提供它。			
			>>> models.Book.objects.aggregate(average_price=Avg('price'))
			{'average_price': 13.233333}
			
			如果你希望生成不止一个聚合，你可以向aggregate()子句中添加另一个参数。所以，如果你也想知道所有图书价格的最大值和最小值，可以这样查询：			
			>>> models.Book.objects.all().aggregate(Avg("price"), Max("price"), Min("price"))
			{'price__avg': 13.233333, 'price__max': Decimal('19.90'), 'price__min': Decimal('9.90')}			
			
2.1.7 元信息：ORM对应的类里面包含另一个Meta类，而Meta类封装了一些数据库的信息。主要字段如下:

	db_table
	ORM在数据库中的表名默认是 app_类名，可以通过db_table可以重写表名。
	
	index_together
	联合索引。
	
	unique_together
	联合唯一索引。
	
	ordering
	指定默认按什么字段排序。
	
	只有设置了该属性，我们查询到的结果才可以被reverse()。			