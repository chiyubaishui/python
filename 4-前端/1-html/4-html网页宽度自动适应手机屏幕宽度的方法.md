<meta name="viewport" content="width=device-width, initial-scale=1.0" />
在网页的<head>中增加以上这句话，可以让网页的宽度自动适应手机屏幕的宽度。

其中：
width=device-width ：表示宽度是设备屏幕的宽度
initial-scale=1.0：表示初始的缩放比例
minimum-scale=0.5：表示最小的缩放比例
maximum-scale=2.0：表示最大的缩放比例
user-scalable=yes：表示用户是否可以调整缩放比例

width：控制 layout viewport 的大小，可以指定的一个值，如 600，或者特殊的值，如 device-width 为设备的宽度（单位为缩放为 100% 时的 CSS 的像素）。viewport  n.（电脑屏幕的）视口，视点  （来自 百度翻译）一、viewport概念关于viewport有两个概念visual viewport跟layout viewport。layout viewport：是网页的所有内容，他可以全部或者部分展示给用户。visual viewport：是当前显示给用户内容的窗口，你可以拖动或者放大缩小网页，这里visual viewport也就是视觉上的窗口，可以理解为设备自己的宽度。二、移动端浏览器加载页面的过程一般来说，在移动浏览器上页面渲染是在 viewport 的页面绘制区域内。手机浏览器把页面放在一个虚拟的“窗口”（viewport）中，通常这个虚拟的“窗口”（viewport）比屏幕宽，这样就不用把每个网页挤到很小的窗口中（这样会破坏没有针对手机浏览器优化的网页的布局），用户可以通过平移和缩放来看网页的不同部分。这个虚拟的“窗口”就是layout viewport。不同的浏览器厂商对于layout viewport的大小定义不同。Safari iPhone: 980px Opera: 850px Android WebKit: 800px IE: 974px三、viewport meta标签作用如果有一个长960的页面，有一个元素是20%（实际解析出来就是192px）。但如果用宽为320px的屏幕打开，这个元素就成了64px，如果这个时候设置的字体大小是12px，在320px的屏幕上就只能显示64/12个字了。鉴于这个问题，定义了viewport meta标签，meta标签的功能就是设置layout viewport为device-width的宽度。它的作用就是创建一个虚拟的窗口（viewport），这个虚拟的窗口就是layout viewport，分辨率接近桌面显示器。这样设置，使得同一个页面在不同的设备上都可以完整正常地显示出来。

