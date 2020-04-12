2.1 ORM 常用字段和参数
	1、AutoField	
		id = models.AutoField(primary_key=True) # 创建一个自增的主键字段
		int自增列，必须填入参数 primary_key=True。当model中如果没有自增列，则自动会创建一个列名为id的列。
	2、CharField	
		name = models.CharField(null=False, max_length=32) # 创建一个varchar(20)类型的不能为空的字段
		字符类型，必须提供max_length参数， max_length表示字符长度。
		null:布尔值，用于表示某个字段是否可以为空。 
		unique：布尔值，用于表示该字段在此表中必须是唯一的。
		
2.2 关系字段
	1、ForeignKey
		外键类型在ORM中用来表示外键关联关系，一般把ForeignKey字段设置在 '一对多'中'多'的一方。
		ForeignKey可以和其他表做关联关系同时也可以和自身做关联关系。
		字段参数
			to 设置要关联的表，表引号
			to_field 设置要关联的表的字段
			related_name 反向操作时，使用的字段名，用于代替原反向查询时的'表名_set'。
			例如：
				class Classes(models.Model):
					name = models.CharField(max_length=32)				
				class Student(models.Model):
					name = models.CharField(max_length=32)
					theclass = models.ForeignKey(to="Classes")
		正向查询：通过学生来查找班级
			ret = models.Student..objects.all() 
			ret[0].theclass.name #theclass其实是一个指向Classes的对象，并不是一个属性值，theclass_id才是一个具体的值，数据库中表的字段就是theclass_id。

