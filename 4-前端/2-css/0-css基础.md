1、CSS如何引入?
	1. 直接写在标签里面 style="样式1;样式2;"
	2. 在head中通过style标签定义
	3. 把样式单独写在css文件中,然后在html文件中通过link标签导入
如一下
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>CSS引入示例</title>
    <!--<style>-->
        <!--p {-->
            <!--color: green;-->   
        <!--}-->
    <!--</style>-->
    <link rel="stylesheet" href="index.css">
</head>
<body>

<!--<p style="color: blue">海燕</p>-->
<p id="p1">海燕</p>
<p id="p2">这个是个黑色的海燕</p>
<p class="c1">这个是个黑色的海燕</p>
<p class="c1">这个是个黑色的海燕</p>
<p class="c1">这个是个黑色的海燕</p>
<p class="c1">这个是个黑色的海燕</p>
<h1>海燕</h1>

</body>
</html>

2、CSS语法  选择器 {样式1;样式2}
p {
    color: red;
    font-size: 18px
}


3、注释：
/*标签选择器*/

4、CSS查找标签的方式(选择器)
1. 基本选择器
	1. 标签选择器     适用于 批量的\统一\默认的样式
	2. ID选择器       适用于 给特定标签设置特定样式
	3. 类选择器       适用于 给某一些标签设置相同的样式
/*标签选择器*/
h1 {
    color: green;
}
/*ID选择器*/
#p2 {
    color: black;
}
/*类选择器*/
.c1 {
    color: yellow;
}
2. 通用选择器
* {
  color: white;
}

3、组合选择器
后代选择器
/*li内部的a标签设置字体颜色*/
li a {
  color: green;
}
儿子选择器
/*选择所有父级是 <div> 元素的 <p> 元素*/
div>p {
  font-family: "Arial Black", arial-black, cursive;
}
毗邻选择器
/*选择所有紧接着<div>元素之后的<p>元素*/
div+p {
  margin: 5px;
}
弟弟选择器
/*i1后面所有的兄弟p标签*/
#i1~p {
  border: 2px solid royalblue;
}

4、属性选择器
/*用于选取带有指定属性的元素。*/
p[title] {
  color: red;
}
/*用于选取带有指定属性和值的元素。*/
p[title="213"] {
  color: green;
}
5、分组和嵌套
分组
当多个元素的样式相同的时候，我们没有必要重复地为每个元素都设置样式，我们可以通过在多个选择器之间使用逗号分隔的分组选择器来统一设置元素样式。 

例如：
div, p {
  color: red;
}
上面的代码为div标签和p标签统一设置字体为红色。

通常，我们会分两行来写，更清晰:
div,
p {
  color: red;
}
嵌套
多种选择器可以混合起来使用，比如：.c1类内部所有p标签设置字体颜色为红色。

.c1 p {
  color: red;
}

6、伪类选择器
/* 未访问的链接 */
a:link {
  color: #FF0000
}

/* 已访问的链接 */
a:visited {
  color: #00FF00
} 

/* 鼠标移动到链接上 */
a:hover {
  color: #FF00FF
} 

/* 选定的链接 */ 
a:active {
  color: #0000FF
}

/*input输入框获取焦点时样式*/
input:focus {
  outline: none;
  background-color: #eee;
}

7、伪元素选择器
first-letter
常用的给首字母设置特殊样式：

p:first-letter {
  font-size: 48px;
  color: red;
}
before
/*在每个<p>元素之前插入内容*/
p:before {
  content:"*";
  color:red;
}
after
/*在每个<p>元素之后插入内容*/
p:after {
  content:"[?]";
  color:blue;
} 
before和after多用于清除浮动