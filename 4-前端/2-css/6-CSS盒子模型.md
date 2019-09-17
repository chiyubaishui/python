CSS盒子模型
margin:            用于控制元素与元素之间的距离；margin的最基本用途就是控制元素周围空间的间隔，从视觉角度上达到相互隔开的目的。
padding:           用于控制内容与边框之间的距离；   
Border(边框):     围绕在内边距和内容外的边框。
Content(内容):   盒子的内容，显示文本和图像。

.margin-test {
  margin-top:5px;
  margin-right:10px;
  margin-bottom:15px;
  margin-left:20px;
}

.margin-test {
  margin: 5px 10px 15px 20px;
}
顺序：上右下左
常见居中：
.mycenter {
  margin: 0 auto;
}

padding内填充
.padding-test {
  padding-top: 5px;
  padding-right: 10px;
  padding-bottom: 15px;
  padding-left: 20px;
}
推荐使用简写：

.padding-test {
  padding: 5px 10px 15px 20px;
}
顺序：上右下左

补充padding的常用简写方式：

提供一个，用于四边；
提供两个，第一个用于上－下，第二个用于左－右；
如果提供三个，第一个用于上，第二个用于左－右，第三个用于下；
提供四个参数值，将按上－右－下－左的顺序作用于四边；

1. margin: 边框之外的距离(多用来调整 标签和标签之间的距离)
2. border边框
3. padding:内容区和边框之间的距离(内填充/内边距)
4. condent: 内容

.c2 {
    height: 100px;
    width: 100%;
    background-color: red;
    margin-top: 100px;
}
虽然设置了宽度100%，但是默认body有个浏览器的css盒子大小，初始化一下
* {
    margin: 0;
    padding: 0;
}