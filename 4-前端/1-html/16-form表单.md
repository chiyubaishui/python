1. form不是from,所有获取用户输入的标签都应该放在form里面, 并且必须要有name属性
2. action属性控制往哪儿提交,method一般都设置成post
3. 提交按钮必须是type=submit,不能是别的类型

一、form表单
	1、基本概念：
		HTML表单是HTML元素中较为复杂的部分，表单往往和脚本、动态页面、数据处理等功能相结合，因此它是制作动态网站很重要的内容。
	2、表单工作原理：
		访问者在浏览有表单的网页时，可填写必需的信息，然后按某个按钮提交。这些信息通过Internet传送到服务器上。 
		服务器上专门的程序对这些数据进行处理，如果有错误会返回错误信息，并要求纠正错误。当数据完整无误后，服务器反馈一个输入完成的信息。
	3、功能：
		表单用于向服务器传输数据，从而实现用户与Web服务器的交互
		表单能够包含input系列标签，比如文本字段、复选框、单选框、提交按钮等等。
		表单还可以包含textarea、select、fieldset和 label标签。

	4、简单例子
		<form action="/add_user/" method="post">
			<p>用户名:
				<input type="text" name="username">
			</p>  
			<p>
				<input type="submit" value="提交">
			</p>
		</form>

	5、表单属性
		属性				描述
		accept-charset	规定在被提交表单中使用的字符集（默认：页面字符集）。
		action			规定向何处提交表单的地址（URL）（提交页面）。
		autocomplete	规定浏览器应该自动完成表单（默认：开启）。
		enctype			规定被提交数据的编码（默认：url-encoded）。
		method			规定在提交表单时所用的 HTTP 方法（默认：GET）。
		name			规定识别表单的名称（对于 DOM 使用：document.forms.name）。
		novalidate		规定浏览器不验证表单。
		target			规定 action 属性中地址的目标（默认：_self）。

二、input标签
	1、<input> 元素会根据不同的 type 属性，变化为多种形态。
		type属性值	表现形式	对应代码
		text		单行输入文本	<input type=text" />
		password	密码输入框	<input type="password"  />
		date		日期输入框	<input type="date" />
		checkbox	复选框	<input type="checkbox" checked="checked"  />
		radio		单选框	<input type="radio"  />
		submit		提交按钮	<input type="submit" value="提交" />
		reset		重置按钮	<input type="reset" value="重置"  />
		button		普通按钮	<input type="button" value="普通按钮"  />
		hidden		隐藏输入框	<input type="hidden"  />
		file		文本选择框	<input type="file" method="post" enctype="multipart/form-data" />  
		enctype 	属性规定在发送到服务器之前应该如何对表单数据进行编码。multipart/form-data	不对字符编码。在使用包含文件上传控件的表单时，必须使用该值。

	2、input属性说明:
		name：表单提交时的“键”，注意和id的区别
		value：表单提交时对应项的值
		placeholder: 提供可描述输入字段预期值的提示信息（hint）,并会在字段获得焦点时消失
		type="button", "reset", "submit"时，为按钮上显示的文本年内容
		type="text","password","hidden"时，为输入框的初始值
		type="checkbox", "radio", "file"，为输入相关联的值
		checked：radio和checkbox默认被选中的项
		readonly：text和password设置只读
		disabled：所有input均适用

三、select标签
	1、例子：
		<form action="" method="post">
		<select name="city" id="city">
			<option value="1">北京</option>
			<option selected="selected" value="2">上海</option>
			<option value="3">广州</option>
			<option value="4">深圳</option>
		</select>
		</form>
		
		optgroup    分组的下拉框
			<select name="from2" id="s2">
				<optgroup label="北京">
					<option value="cp">昌平</option>
					<option value="cy">朝阳</option>
					<option value="hd">海淀</option>
					<option value="ft">丰台</option>
				</optgroup>
				<optgroup label="上海">
					<option value="pdxq">浦东新区</option>
					<option value="mhq">闵行区</option>
					<option value="hpq">黄浦区</option>
				</optgroup>
				<optgroup label="四川">
					<option value="pzh">攀枝花</option>
					<option value="zg">自贡</option>
					<option value="my">绵阳</option>
				</optgroup>
			</select>
	
	2、属性说明：
		multiple：布尔属性，设置后为多选，否则默认单选
		disabled：禁用
		selected：默认选中该项
		value：定义提交时的选项值

四、label标签
	定义：<label> 标签为 input 元素定义标注（标记）。
	说明：
	label 元素不会向用户呈现任何特殊效果。
	<label> 标签的 for 属性值应当与相关元素的 id 属性值相同。
	<form action="">
		<label for="username">用户名</label>
		<input type="text" id="username" name="username">
	</form>

五、textarea多行文本
<textarea name="memo" id="memo" cols="30" rows="10">
  默认内容
</textarea>
属性说明：

name：名称
rows：行数
cols：列数
disabled：禁用