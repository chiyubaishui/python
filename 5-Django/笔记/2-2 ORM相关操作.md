2.2 ORM相关操作
2.2.1 一般操作
	<1> all(): 查询所有结果,返回QuerySet对象,是查询集，可以通过方法查询具体的值
		ret = models.UserInfo.objects.all() 
		ret,ret[0],ret[0].id #<QuerySet [<UserInfo: UserInfo object>]>,UserInfo object 1  QuerySet,具体的对象，具体的对象的属性（数值）
		
2.2.2 方法
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