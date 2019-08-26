1、引入js
Script标签内写代码
<script>
  // 在这里写你的JS代码
</script>
引入额外的JS文件
<script src="myscript.js"></script>

2、注释
// 单行注释

/*
多行注释
*/

3、结束符
JavaScript中的语句要以分号（;）为结束符。

4、变量声明（动态类型）
JavaScript的变量名可以使用_，数字，字母，$组成，不能以数字开头。
声明变量使用 var 变量名; 的格式来进行声明
var name = "Alex";
var age = 18;
注意：
变量名是区分大小写的。
推荐使用驼峰式命名规则。
保留字不能用做变量名。

补充：
ES6新增了let命令，用于声明变量。其用法类似于var，但是所声明的变量只在let命令所在的代码块内有效。例如：for循环的计数器就很适合使用let命令。
for (let i=0;i<arr.length;i++){...}
ES6新增const用来声明常量。一旦声明，其值就不能改变。
const PI = 3.1415;
PI // 3.1415
PI = 3
// TypeError: "PI" is read-only


5、JavaScript数据类型
数值(Number)
JavaScript不区分整型和浮点型，就只有一种数字类型。
var a = 12.34;
var b = 20;
var c = 123e5;  // 12300000
var d = 123e-5;  // 0.00123
还有一种NaN，表示不是一个数字（Not a Number）。
常用方法：
parseInt("123")  // 返回123
parseInt("ABC")  // 返回NaN,NaN属性是代表非数字值的特殊值。该属性用于指示某个值不是数字。

字符串(String)
var a = "Hello"
var b = "world;
var c = a + b; 
console.log(c);  // 拼接字符串一般使用“+”，得到Helloworld

常用方法：

方法  	说明
.length	返回长度
.trim()	移除空白
.trimLeft()	移除左边的空白
.trimRight()	移除右边的空白
.charAt(n)	返回第n个字符
.concat(value, ...)	拼接
.indexOf(substring, start)	子序列位置
.substring(from, to)	根据索引获取子序列
.slice(start, end)	切片
.toLowerCase()	小写
.toUpperCase()	大写
.split(delimiter, limit)	分割

string.slice(start, stop)和string.substring(start, stop)：

.substring(from, to)和.slice(start, end)两者的相同点：
如果start等于end，返回空字符串
如果stop参数省略，则取到字符串末
如果某个参数超过string的长度，这个参数会被替换为string的长度

substirng()的特点：
如果 start > stop ，start和stop将被交换
如果参数是负数或者不是数字，将会被0替换

silce()的特点：
如果 start > stop 不会交换两者
如果start小于0，则切割从字符串末尾往前数的第abs(start)个的字符开始(包括该位置的字符)
如果stop小于0，则切割在从字符串末尾往前数的第abs(stop)个字符结束(不包含该位置字符)

6、布尔值(Boolean)
区别于Python，true和false都是小写。
var a = true;
var b = false;