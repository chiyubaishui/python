3.2 Django的view（视图）
3.2.1 基本介绍
	一个视图函数（类），简称视图，是一个简单的Python 函数（类），它接受Web请求并且返回Web响应。
	响应可以是一张网页的HTML内容，一个重定向，一个404错误，一个XML文档，或者一张图片。
	无论视图本身包含什么逻辑，都要返回响应。代码写在哪里也无所谓，只要它在你当前项目目录下面。除此之外没有更多的要求了——可以说“没有什么神奇的地方”。为了将代码放在某处，大家约定成俗将视图放置在项目（project）或应用程序（app）目录中的名为views.py的文件中。

3.2.1 CBV和FBV
	我们之前写过的都是基于函数的view，就叫FBV。还可以把view写成基于类的。

3.2.3 Request对象和Response对象
	1、request对象
		当一个页面被请求时，Django就会创建一个包含本次请求原信息的HttpRequest对象。
		Django会将这个对象自动传递给响应的视图函数，一般视图函数约定俗成地使用 request 参数承接这个对象。	
		请求相关的常用值
			path_info     返回用户访问url，不包括域名
			method        请求中使用的HTTP方法的字符串表示，全大写表示。
			GET              包含所有HTTP  GET参数的类字典对象
			POST           包含所有HTTP POST参数的类字典对象
			body            请求体，byte类型 request.POST的数据就是从body里面提取到的
			getlist			post提交的数据是多个值的，如多选的checkbox和多选的select
	2、上传文件实例：
		<form action="/upload/" method="post" enctype="multipart/form-data">
			<input type="file" name="upload_file">
			<input type="submit" value="开始上传">
		</form>
		
		def upload(request):
			"""
			保存上传文件前，数据需要存放在某个位置。默认当上传文件小于2.5M时，django会将上传文件的全部内容读进内存。从内存读取一次，写磁盘一次。
			但当上传文件很大时，django会把上传文件写到临时文件中，然后存放到系统临时文件夹中。
			:param request: 
			:return: 
			"""
			if request.method == "POST":
				# 从请求的FILES中获取上传文件的文件名，file为页面上type=files类型input的name属性值
				filename = request.FILES["upload_file"].name
				# 在项目目录下新建一个文件
				with open(filename, "wb") as f:
					# 从上传的文件对象中一点一点读
					for chunk in request.FILES["upload_file"].chunks():
						# 写入本地文件
						f.write(chunk)
				return HttpResponse("上传OK")
	3、Response对象：
		1. HttpResponse        --> 返回字符串内容
		2. render              --> 返回一个html页面             
		3. redirect            --> 返回一个重定向（告诉浏览器再去访问另外的网址）		
		4. JsonResponse
			def json_test(request):
				data = {"name": "小黑", "age": 18}
				data2 = [11, 22, 33, 44]
				# import json
				# data_str = json.dumps(data2)  # 把data序列化成json格式的字符串
				# return HttpResponse(data_str)
			
				from django.http import JsonResponse
				return JsonResponse(data2, safe=False) #只能接受字典形式
				
		扩展阅读： 
			临时重定向（响应状态码：302）和永久重定向（响应状态码：301）对普通用户来说是没什么区别的，它主要面向的是搜索引擎的机器人。
			A页面临时重定向到B页面，那搜索引擎收录的就是A页面。
			A页面永久重定向到B页面，那搜索引擎收录的就是B页面。