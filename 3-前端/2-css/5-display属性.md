用于控制HTML元素的显示效果。

值	             意义
display:"none"	HTML文档中元素存在，但是在浏览器中不显示。一般用于配合JavaScript代码使用。
display:"block"	默认占满整个页面宽度，如果设置了指定宽度，则会用margin填充剩下的部分。
display:"inline"	按行内元素显示，此时再设置元素的width、height、margin-top、margin-bottom和float属性都不会有什么影响。
display:"inline-block"	使元素同时具有行内元素和块级元素的特点。

display:"none"与visibility:hidden的区别：
visibility:hidden: 可以隐藏某个元素，但隐藏的元素仍需占用与未隐藏之前一样的空间。也就是说，该元素虽然被隐藏了，但仍然会影响布局。
display:none: 可以隐藏某个元素，且隐藏的元素不会占用任何空间。也就是说，该元素不但被隐藏了，而且该元素原本占用的空间也会从页面布局中消失。