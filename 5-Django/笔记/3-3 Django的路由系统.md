3.3 Django的路由系统
3.3.1 基本介绍
	URL配置(URLconf)就像Django 所支撑网站的目录。它的本质是URL与要为该URL调用的视图函数之间的映射表。
	基本格式：
		from django.conf.urls import url
			urlpatterns = [
				url(正则表达式, views视图函数，参数，别名),
			]
		Django 2.0版本中的路由系统url已经替换成path
	参数说明：
		正则表达式：一个正则表达式字符串
		views视图函数：一个可调用对象，通常为一个视图函数或一个指定视图函数路径的字符串
		参数：可选的要传递给视图函数的默认参数（字典形式）
		别名：一个可选的name参数	
3.3.2 正则表达式详解
	1、基本配置
		from django.conf.urls import url
		from . import views
		urlpatterns = [
			url(r'^articles/2003/$', views.special_case_2003),
			url(r'^articles/([0-9]{4})/$', views.year_archive),
			url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
			url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
		]
	注意事项：
		urlpatterns中的元素按照书写顺序从上往下逐一匹配正则表达式，一旦匹配成功则不再继续。
		若要从URL中捕获一个值，只需要在它周围放置一对圆括号（分组匹配），一对括号相当于一个参数传递给后端，后端的函数要接受。
		不需要添加一个前导的反斜杠，因为每个URL 都有。例如，应该是^articles 而不是 ^/articles。
		每个正则表达式前面的'r' 是可选的但是建议加上。
		是否开启URL访问地址后面不为/跳转至带有/的路径的配置项，APPEND_SLASH=True
		
	2、分组命名匹配
		上面的示例使用简单的正则表达式分组匹配（通过圆括号）来捕获URL中的值并以位置参数形式传递给视图。
		在更高级的用法中，可以使用分组命名匹配的正则表达式组来捕获URL中的值并以关键字参数形式传递给视图。
		在Python的正则表达式中，分组命名正则表达式组的语法是(?P<name>pattern)，其中name是组的名称，pattern是要匹配的模式。
		
		捕获的参数永远都是字符串
			每个在URLconf中捕获的参数都作为一个普通的Python字符串传递给视图，无论正则表达式使用的是什么匹配方式。例如，下面这行URLconf 中：
			url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
			传递到视图函数views.year_archive() 中的year 参数永远是一个字符串类型
			
		视图函数中指定默认值
			# urls.py中
			from django.conf.urls import url			
			from . import views			
			urlpatterns = [
				url(r'^blog/$', views.page),
				url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
			]			
		# views.py中，可以为num指定默认值
			def page(request, num="1"):
				pass
		在上面的例子中，两个URL模式指向相同的view - views.page - 但是第一个模式并没有从URL中捕获任何东西。
		如果第一个模式匹配上了，page()函数将使用其默认参数num=“1”,如果第二个模式匹配，page()将使用正则表达式捕获到的num值。
		
	3、URLconf匹配的位置
		URLconf 在请求的URL 上查找，将它当做一个普通的Python 字符串。不包括GET和POST参数以及域名。
		例如，http://www.example.com/myapp/ 请求中，URLconf 将查找myapp/。
		在http://www.example.com/myapp/?page=3 请求中，URLconf 仍将查找myapp/。
		URLconf 不检查请求的方法。换句话讲，所有的请求方法 —— 同一个URL的POST、GET、HEAD等等 —— 都将路由到相同的函数。
		
	4、include其他的URLconfs
		from django.conf.urls import include, url
		urlpatterns = [
		url(r'^admin/', admin.site.urls),
		url(r'^blog/', include('blog.urls')),  # 可以包含其他应用的URLconfs文件
		]
		
3.3.3 命名URL和URL反向解析
	可以给我们的URL匹配规则起个名字，这样我们以后就不需要写死URL代码了，只需要通过名字来调用当前的URL。
	举个简单的例子：
		url(r'^home', views.home, name='home'),  # 给我的url匹配模式起名为 home
		url(r'^index/(\d*)', views.index, name='index'),  # 给我的url匹配模式起名为index
	这样，在模板里面可以这样引用：
	{% url 'home' %}，那么url中r'^home'不管怎么变化，都可以找到对应的页面
	
	在views函数中可以这样引用：
	from django.urls import reverse
	ret = reverse("home")
	ret = reverse("home",kwargs={})
	return redirect(ret)
	
3.3.4 命名空间模式
	即使不同的APP使用相同的URL名称，URL的命名空间模式也可以让你唯一反转命名的URL。
	project中的urls.py	
	from django.conf.urls import url, include	
	urlpatterns = [
		url(r'^app01/', include('app01.urls', namespace='app01')),
		url(r'^app02/', include('app02.urls', namespace='app02')),
	]
	
	模板中使用：
	{% url 'app01:detail' pk=12 pp=99 %}
	views中的函数中使用	
	v = reverse('app01:detail', kwargs={'pk':11})