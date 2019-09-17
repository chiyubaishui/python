meta是head区的一个辅助性标签。其主要作用有：搜索引擎优化（SEO），定义页面使用语言，自动刷新并指向新的页面，实现网页转换时的动态效果，控制页面缓冲，网页定级评价，控制网页显示的窗口等！

meta标签共有两个属性，它们分别是http-equiv属性和name属性。

http-equiv属性
1、<meta http-equiv="Content-Type" contect="text/html";charset=gb_2312-80">和 <meta http-equiv="Content-Language" contect="zh-CN">用以说明主页制作所使用的文字以及语言；又如英文是ISO-8859-1字符集，还有BIG5、utf-8、shift-Jis、Euc、Koi8-2等字符集；
2、<meta http-equiv="Refresh" contect="n;url=http://yourlink">定时让网页在指定的时间n内，跳转到页面http://yourlink；
3、<meta http-equiv="Expires" contect="Mon,12 May 2001 00:20:00 GMT">可以用于设定网页的到期时间，一旦过期则必须到服务器上重新调用。需要注意的是必须使用GMT时间格式；
4、<meta http-equiv="Pragma" contect="no-cache">是用于设定禁止浏览器从本地机的缓存中调阅页面内容，设定后一旦离开网页就无法从Cache中再调出；
5、<meta http-equiv="set-cookie" contect="Mon,12 May 2001 00:20:00 GMT">cookie设定，如果网页过期，存盘的cookie将被删除。需要注意的也是必须使用GMT时间格式；
6、<meta http-equiv="Pics-label" contect="">网页等级评定，在IE的internet选项中有一项内容设置，可以防止浏览一些受限制的网站，而网站的限制级别就是通过meta属性来设置的；
7、<meta http-equiv="windows-Target" contect="_top">强制页面在当前窗口中以独立页面显示，可以防止自己的网页被别人当作一个frame页调用；
8、<meta http-equiv="Page-Enter" contect="revealTrans(duration=10,transtion= 50)">和<meta http-equiv="Page-Exit" contect="revealTrans(duration=20，transtion=6)">设定进入和离开页面时的特殊效果，这个功能即FrontPage中的“格式/网页过渡”，不过所加的页面不能够是一个frame页面。
 
2、name属性
name属性主要用于描述网页，与之对应的属性值为content，content中的内容主要是便于搜索引擎机器人查找信息和分类信息用的。

meta标签的name属性语法格式是：

1
<meta name="参数" content="具体的参数值">。
其中name属性主要有以下几种参数：　

A、Keywords(关键字)　

说明：keywords用来告诉搜索引擎你网页的关键字是什么。

举例：

1
<meta name="keywords" content="">
B、description(网站内容描述)

说明：description用来告诉搜索引擎你的网站主要内容。

举例：

1
<meta name="description" content="">
C、robots(机器人向导)

说明：robots用来告诉搜索机器人哪些页面需要索引，哪些页面不需要索引。

content的参数有all,none,index,noindex,follow,nofollow。默认是all。

举例：

1
<meta name="robots" content="none">
具体参数如下：

信息参数为all：文件将被检索，且页面上的链接可以被查询；

信息参数为none：文件将不被检索，且页面上的链接不可以被查询；

信息参数为index：文件将被检索；

信息参数为follow：页面上的链接可以被查询；

信息参数为noindex：文件将不被检索，但页面上的链接可以被查询；

信息参数为nofollow：文件将被检索，但页面上的链接不可以被查询；

D、author(作者)

说明：标注网页的作者

举例：

1
<meta name="author" content="jesse131work@163.com">
E、generator

1
<meta name="generator" content="信息参数"/>
meta标签的generator的信息参数，代表说明网站的采用的什么软件制作。

F、copyright

1
<meta name="copyright" content="信息参数">
meta标签的copyright的信息参数，代表说明网站版权信息。

G、revisit-after

1
<meta name="revisit-after" content="7days">
revisit-after代表网站重访,7days代表7天，依此类推。

 

 

Meta Property=og标签是什么呢?
og是一种新的HTTP头部标记，即Open Graph Protocol：

The Open Graph Protocol enables any web page to become a rich object in a social graph.+ n3 }

即这种协议可以让网页成为一个“富媒体对象”。
用了Meta Property=og标签，就是你同意了网页内容可以被其他社会化网站引用等，目前这种协议被SNS网站如Fackbook、renren采用。
SNS已经成为网络上的一大热门应用，优质的内容通过分享在好友间迅速传播。为了提高站外内容的传播效率，2010年F8会议上Facebook公布 了一套开放内容协议(Open Graph Protocol)，任何网页只要遵守该协议，SNS就能从页面上提取最有效的信息并呈现给用户。