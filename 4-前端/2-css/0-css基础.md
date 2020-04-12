0、CSS语法
每个CSS样式由两个组成部分：选择器和声明。声明又包括属性和属性值。每个声明之后用分号结束。
CSS语法  选择器 {样式1;样式2}
<p style="color: red">Hello world.</p>
p为选择器，style="color: red"为声明，color为属性，red为值

1、CSS如何引入?
	1. 直接写在标签里面 style="样式1;样式2;"
	2. 在head中通过style标签定义
	3. 把样式单独写在css文件中,然后在html文件中通过link标签导入
如下
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

2、注释：
/*标签选择器*/


