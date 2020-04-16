request对象
当一个页面被请求时，Django就会创建一个包含本次请求原信息的HttpRequest对象。
Django会将这个对象自动传递给响应的视图函数，一般视图函数约定俗成地使用 request 参数承接这个对象。

请求相关的常用值
path_info     返回用户访问url，不包括域名
method        请求中使用的HTTP方法的字符串表示，全大写表示。
GET              包含所有HTTP  GET参数的类字典对象
POST           包含所有HTTP POST参数的类字典对象
body            请求体，byte类型 request.POST的数据就是从body里面提取到的
getlist			post提交的数据是多个值的，如多选的checkbox和多选的select