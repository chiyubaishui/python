2.2 ORM相关操作
2.2.1 一般操作
	<1> all(): 查询所有结果,返回QuerySet对象,是查询集，可以通过方法查询具体的值
		ret = models.UserInfo.objects.all() 
		ret,ret[0],ret[0].id #<QuerySet [<UserInfo: UserInfo object>]>,UserInfo object 1  QuerySet,具体的对象，具体的对象的属性（数值）
	<2> get(**kwargs):  返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。
		ret = models.UserInfo.objects.get() 
	<3> filter(**kwargs): 它包含了与所给筛选条件相匹配的对象
		ret = models.Person.objects.filter(id=100)  # 不存在返回一个空的QuerySet，不会报错
		ret = models.Person.objects.filter(id=1)[0] # 就算查询的结果只有一个，返回的也是QuerySet，我们要用索引的方式取出第一个元素
	<4> exclude(**kwargs):它包含了与所给筛选条件不匹配的对象,返回QuerySet对象
	<5> values(*field):返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列model的实例化对象(object)，而是一个可迭代的字典序列.不写字段名，默认查询所有字段
	<6> values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列,不写字段名，默认查询所有字段.
	<7> order_by(*field):对查询结果排序
	<8> reverse():        对查询结果反向排序，请注意reverse()通常只能在具有已定义顺序的QuerySet上调用(在model类的Meta中指定ordering或调用order_by()方法)。
	<9> distinct():            从返回结果中剔除重复纪录(如果你查询跨越多个表，可能在计算QuerySet时得到重复的结果。此时可以使用distinct()，注意只有在PostgreSQL中支持按字段去重。) 
	<10> count():              返回数据库中匹配查询(QuerySet)的对象数量。
	<11> first():              返回第一条记录 
	<12> last():               返回最后一条记录 
	<13> exists():             如果QuerySet包含数据，就返回True，否则返回False
	
	总结：
	返回QuerySet对象的方法有：
		all()
		filter()
		exclude()
		order_by()
		reverse()
		distinct()
	特殊的QuerySet：
		values()       返回一个可迭代的字典序列
		values_list() 返回一个可迭代的元祖序列
	返回具体对象的：
		get()
		first()
		last()
	返回布尔值的方法有：
		exists()
	返回数字的方法有：
		count()
		
2.2.2 单表查询之神奇的双下划线
	models.Tb1.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值
	models.Tb1.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
	models.Tb1.objects.exclude(id__in=[11, 22, 33])  # not in
	models.Tb1.objects.filter(name__contains="ven")  # 获取name字段包含"ven"的
	models.Tb1.objects.filter(name__icontains="ven") # icontains大小写不敏感 
	models.Tb1.objects.filter(id__range=[1, 3])      # id范围是1到3的，等价于SQL的bettwen and 
	类似的还有：startswith，istartswith, endswith, iendswith　
	date字段还可以：
	models.Class.objects.filter(first_day__year=2017)

2.2.3 方法
	<1> create()：创建一个新的对象，保存对象，自动提交，并将它添加到关联对象集之中，返回新创建的对象。
		models.UserInfo.objects.create(name="张三")
	<2> delete(): 删除一个对象。
		del_id = request.GET.get("id", None) #从GET请求的参数里面拿到将要删除的数据的ID值，request.GET返回的是<QueryDict>
		del_obj = models.Publisher.objects.get(id=del_id) # 根据id值查找到数据
		del_obj.delete() # 删除
	<3> save(): 保存一个对象。
		edit_publisher = models.Publisher.objects.get(id=edit_id)
        edit_publisher.name = new_name
        edit_publisher.save()  # 把修改提交到数据库
	<3> set()：更新model对象的关联对象。
		new_book = request.POST.getlist("add_book_name")
		new_author_obj.book.set(new_book)