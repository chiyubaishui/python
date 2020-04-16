3.1 Django模板系统
3.1.0 常用语法:
	只需要记两种特殊符号：
	{{  }}和 {% %}
	变量相关的用{{}}，逻辑相关的用{%%}。
3.1.1 变量
	在Django的模板语言中按此语法使用：{{ 变量名 }}。
	当模版引擎遇到一个变量，它将计算这个变量，然后用结果替换掉它本身。 变量的命名包括任何字母数字以及下划线 ("_")的组合。 变量名称中不能有空格或标点符号。

	点（.）在模板语言中有特殊的含义。当模版系统遇到点(".")，它将以这样的顺序查询：
	字典查询（Dictionary lookup）
	属性或方法查询（Attribute or method lookup）
	数字索引查询（Numeric index lookup）
	
	取name中的第一个参数	{{ name.0 }}
	取字典中key的值		{{ d.name }}
	取对象的name属性 		{{ person_list.0.name }}
	操作只能调用不带参数的方法	{{ person_list.0.dream }}

	注意事项：
		如果计算结果的值是可调用的，它将被无参数的调用。 调用的结果将成为模版的值。
		如果使用的变量不存在， 模版系统将插入 string_if_invalid 选项的值， 它被默认设置为'' (空字符串)。
		
3.1.2 Filters（过滤器）
	在Django的模板语言中，通过使用 过滤器 来改变变量的显示。
	过滤器的语法： {{ value|filter_name:参数 }}
	使用管道符"|"来应用过滤器。
	注意事项：
		1、过滤器支持“链式”操作。即一个过滤器的输出作为另一个过滤器的输入。
		2、过滤器可以接受参数，例如：{{ sss|truncatewords:30 }}，这将显示sss的前30个词。
		3、过滤器参数包含空格的话，必须用引号包裹起来。比如使用逗号和空格去连接一个列表中的元素，如：{{ list|join:', ' }}
		4、'|'左右没有空格没有空格没有空格
		
	Django的模板语言中提供了大约六十个内置过滤器:
	1、default：如果一个变量是false或者为空，使用给定的默认值。 否则，使用变量的值。
		{{ value|default:"nothing"}}  #如果value没有传值或者值为空的话就显示nothing
	2、length：返回值的长度，作用于字符串和列表。
		{{ value|length }}  #返回value的长度，如 value=['a', 'b', 'c', 'd']的话，就显示4.
	3、filesizeformat：将值格式化为一个 “人类可读的” 文件尺寸 （例如 '13 KB', '4.1 MB', '102 bytes', 等等）。例如：
		{{ value|filesizeformat }}  #如果 value 是 123456789，输出将会是 117.7 MB。
	4、slice:切片，数字无法切
		{{value|slice:"2:-1"}}
	5、date：格式化
		{{ value|date:"Y-m-d H:i:s"}}
	6、safe：Django的模板中会对HTML标签和JS等语法标签进行自动转义，原因显而易见，这样是为了安全。但是有的时候我们可能不希望这些HTML元素被转义，比如我们做一个内容管理系统，后台添加的文章中是经过修饰的，这些修饰可能是通过一个类似于FCKeditor编辑加注了HTML修饰符的文本，如果自动转义的话显示的就是保护HTML标签的源文件。为了在Django中关闭HTML的自动转义有两种方式，如果是一个单独的变量我们可以通过过滤器“|safe”的方式告诉Django这段代码是安全的不必转义。
		value = "<a href='#'>点我</a>"
		{{ value|safe}}
	7、truncatechars：如果字符串字符多于指定的字符数量，那么会被截断。截断的字符串将以可翻译的省略号序列（“...”）结尾。
	参数：截断的字符数
		{{ value|truncatechars:9}}
	8、truncatewords：在一定数量的字后截断字符串。
		{{ value|truncatewords:9}}
	9、cut：移除value中所有的与给出的变量相同的字符串
		{{ value|cut:' ' }}  #如果value为'i love you'，那么将输出'iloveyou'.
	10、join：使用字符串连接列表，例如Python的str.join(list)
	11、timesince：将日期格式设为自该日期起的时间（例如，“4天，6小时”）。
	采用一个可选参数，它是一个包含用作比较点的日期的变量（不带参数，比较点为现在）。 例如，如果blog_date是表示2006年6月1日午夜的日期实例，并且comment_date是2006年6月1日08:00的日期实例，则以下将返回“8小时”：
	{{ blog_date|timesince:comment_date }}
	分钟是所使用的最小单位，对于相对于比较点的未来的任何日期，将返回“0分钟”。
	12、timeuntil：似于timesince，除了它测量从现在开始直到给定日期或日期时间的时间。 例如，如果今天是2006年6月1日，而conference_date是保留2006年6月29日的日期实例，则{{ conference_date | timeuntil }}将返回“4周”。
	使用可选参数，它是一个包含用作比较点的日期（而不是现在）的变量。 如果from_date包含2006年6月22日，则以下内容将返回“1周”：
	{{ conference_date|timeuntil:from_date }}

	13、自定义filter
		自定义过滤器只是带有一个或两个参数的Python函数:

		变量（输入）的值 - -不一定是一个字符串
		参数的值 - 这可以有一个默认值，或完全省略
		例如，在过滤器{{var | foo:'bar'}}中，过滤器foo将传递变量var和参数“bar”。

 

		1、自定义filter代码文件摆放位置：在app01下面新建一个 python package
		app01/
			__init__.py
			models.py
			templatetags/  # 在app01下面新建一个package package
				__init__.py
				app01_filters.py  # 建一个存放自定义filter的文件
			views.py
		
		2、编写自定义filter:
			from django import template
			register = template.Library()
			
			
			@register.filter(name="cut")
			def cut(value, arg): #第一个参数永远就是前端页面里管道前面的变量，第二个参数是filter后面的参数
				return value.replace(arg, "")
			
			
			@register.filter(name="addSB")
			def add_sb(value):
				return "{} SB".format(value)
			
		3、使用自定义filter，需要重启一下，重新加载一下
		{# 先导入我们自定义filter那个文件 #}
		{% load app01_filters %}
		
		{# 使用我们自定义的filter #}
		{{ somevariable|cut:"0" }}
		{{ d.name|addSB }}
		
3.1.3 tag
	1、for循环
	普通for循环
		<ul>
		{% for user in user_list %}
			<li>{{ user.name }}</li>
		{% endfor %}
		</ul>
	for循环可用的一些参数：
		Variable			Description
		forloop.counter		当前循环的索引值（从1开始）
		forloop.counter0	当前循环的索引值（从0开始）
		forloop.revcounter	当前循环的倒序索引值（从1开始）
		forloop.revcounter0	当前循环的倒序索引值（从0开始）
		forloop.first		当前循环是不是第一次循环（布尔值）
		forloop.last		当前循环是不是最后一次循环（布尔值）
		forloop.parentloop	本层循环的外层循环，是一个对象，有forloop.parentloop.counter,forloop.parentloop.first等
	for ... empty
		<ul>
		{% for user in user_list %}
			<li>{{ user.name }}</li>
		{% empty %}
			<li>空空如也</li>
		{% endfor %}
		</ul>

	2、if判断
	if,elif和else
		{% if user_list %}
			用户人数：{{ user_list|length }}
		{% elif black_list %}
			黑名单数：{{ black_list|length }}
		{% else %}
			没有用户
		{% endif %}
	if语句支持 and 、or、==、>、<、!=、<=、>=、in、not in、is、is not判断。

	3、with
		定义一个中间变量，多用于给一个复杂的变量起别名。
		注意等号左右不要加空格。

		{% with total=business.employees.count %}
			{{ total }} employee{{ total|pluralize }}
		{% endwith %}
		或		
		{% with business.employees.count as total %}
			{{ total }} employee{{ total|pluralize }}
		{% endwith %}
	
	4、注释
		{# ... #}
		
	5、母板：把多个页面公用的部分提取出来，放在一个母版里面。其他的页面只需要继承母版就可以了
		1)继承母板：在子页面中在页面最上方使用下面的语法来继承母板。
		{% extends 'layouts.html' %}
		2)在子页面中通过定义母板中的block名来对应替换母板中相应的内容。
		通过在母板中使用{% block  xxx %}来定义"块"。		
			{% block page-main %}
			...
			{% endblock %}
			
		使用母版和继承的注意事项：
			1. {% extends 'base.html' %} --> 母版文件:base.html要加引号
			2. {% extends 'base.html' %} --> 必须放在子页面的第一行！！！
			3. 可以在base.html中定义很多block，通常我们会额外定义page-css和page-js两个块
			4. view.py相应的函数中返回的是对应的子页面文件 不是母版base.html
			
	6、组件
		可以将常用的页面内容如导航条，页尾信息等组件保存在单独的文件中，然后在需要使用的地方按如下语法导入即可。
		{% include 'navbar.html' %}
		
	7、静态文件相关 {% static %}
		{% load static %}
		<img src="{% static "images/hi.jpg" %}" alt="Hi!" />
		
		引用JS文件时使用：		
		{% load static %}
		<script src="{% static "mytest.js" %}"></script>
		
		某个文件多处被用到可以存为一个变量		
		{% load static %}
		{% static "images/hi.jpg" as myphoto %}
		<img src="{{ myphoto }}"></img>
		
		另一种方式拼接：{% get_static_prefix %}
		{% load static %}
		<img src="{% get_static_prefix %}images/hi.jpg" alt="Hi!" />
		或者		
		{% load static %}
		{% get_static_prefix as STATIC_PREFIX %}
		
		<img src="{{ STATIC_PREFIX }}images/hi.jpg" alt="Hi!" />
		<img src="{{ STATIC_PREFIX }}images/hi2.jpg" alt="Hello!" />
			