meta name="description" content="" 作用讲解
 一、语法： 
<meta name="name" content="string"> 
二、参数解析： 
1）name项：常用的选项有Keywords(关键字) ，description(网站内容描述)，author(作者)，robots(机器人向导)等。 
2）http-equiv项：可用于代替name项，常用的选项有Expires(期限)，Pragma(cache模式)，Refresh(刷新)，Set-Cookie(cookie设定)，Window-target(显示窗口的设定)，content-Type(显示字符集的设定)等。 
3）content项：根据name项或http-equiv项的定义来决定此项填写什么样的字符串。 
三、应用 
1、告诉浏览器网页所识别的文件类型及语言类型，比如说，我们要让浏览器识别HTM/HTML类型的简体中文网面，我们可以这样写： 
< Meta http-equiv="Content-Type" content="text/html; charset=gb2312" > 
2、让一些搜索引擎搜索到你的网页，代码可以这样写： 
< Meta Name=" Keywords" Content="网页关键字" > 
< Meta Name=" description" Content="网页描述文字" > 
要达到自动搜索引擎真正能方便地搜索到你的网页还得注意以下几点： 
A、既要定义meta标记项，又要将首页正文的前200个字符定义成反映主页主题的文字。因为有些导航台在标引meta项中的关键词的同时，还要标引正文中的前200个字符。如：altavista。所以，有些人在注册完导航台后去检查注册结果时，发现导航台中的描述并不是你所希望的，而是诸如版权说明之类的文字。产生这一现象的原因就是没有注意到这一点。 
B、将定义关键词的meta标记项放在定义描述的meta项之前。如： 
<meta type="keywords" content=".......,...,...">                       <!--  关键词间用逗号分隔-->
<meta type="description" content="...,....,..."> 
C、将最重要的关键词放在最前面，让相关的关键词相邻。全小写与首字母大写并存，因为有的导航台在标引时对字符的大小写是敏感的。包括标点符号不要超过250个单词 
D、首页最好不用frame结构，因为frame将屏幕划分成多个窗口后，导航台不能智能地选择正确的窗口中的主页去标引。 E、由于keywords的特性方便搜索器搜索，也会导致搜索排行的变化（越多关键词越容易上排行前列），故而现在搜索器大多不再将keywords考虑进搜索算法中，所以keywords现在少用很多，一般可以不写
3、让一个页面过上一定的时间，自动转到另一个页面或者站点去，如： 
< Meta HTTP-EQUIV="refresh" content="6; url=http://hi.baidu.com/tesalo/" > 
content中的6表示时间，单位为秒，url=后面是你要转向的网址，若是与你当前网页在同一目录下，可以直接写上文件名，如： 
< Meta HTTP-EQUIV="refresh" content="6; url=page1.htm" > 
4、让网页每隔一段时间刷新一次，若要10秒刷新一次，代码这样写： 
<meta http-equiv="refresh" content="10"> 
5、通过Meta可以让你进入页面时产生一些特殊效果，具体应用如下： 
< meta http-equiv="Page-Enter" content= "revealTrans(Duration=5.0,Transition=n)" > 其中，duration为变化速度，transtion为效果方式，n的取值范围为0-23，具体的意义如下： 
0 矩形缩小              1 矩形扩大              2 圆形缩小 
3 圆形扩大              4 下到上                  5 上到下 
6 左到右                 7 右到左                   8 竖百叶窗 
9 横百叶窗             10 错位横百叶窗     11 错位竖百叶窗 
12 点                      13 左右到中间        14 中间到左右 
15 中间到上下        16 上下到中间       17 右下到左上 
18 右上到左下        19 左上到右下        20 左下到右上 
21 横条                   22 竖条                  23 以上 24种随机选择一种 
PS:这个东西貌似只有IE8会实现，其他浏览器不会，有人说是IE6，有人说IE8，而高于IE8的浏览器都不行，像360,谷歌，火狐都不行，所以可以不用啦，效果什么的交给css吧
6、标注作者： 
<meta name="author" content="二度空间"> 
7、控制页面缓冲，如不要页面缓冲的代码这样写： 
<meta http-equiv="Cache-Control" CONTENT="no-cache">