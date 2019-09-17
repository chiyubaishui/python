<meta name="referrer" content="origin" />
referer是什么： 
我们知道，在页面引入图片、JS 等资源，或者从一个页面跳到另一个页面，都会产生新的 HTTP 请求，浏览器一般都会给这些请求头加上表示来源的 Referrer 字段。Referrer 在分析用户来源时很有用，有着广泛的使用。但 URL 可能包含用户敏感信息，如果被第三方网站拿到很不安全（例如之前不少 Wap 站把用户 SESSION ID 放在 URL 中传递，第三方拿到 URL 就可以看到别人登录后的页面）。之前浏览器会按自己的默认规则来决定是否加上 Referrer。
简单来讲，referer的作用就是记录你在访问一个目标网站时，在访问前你的原网站的地址， 比如用Chrome从知乎的某个板块到另外一个，那么你在的这个网站就是原网站，按F12，选中Network选项， 从页面内进入一个网站，可以从这个网站的header即头信息中，看到referer就是原来的那个网站。
2014 年，W3C 的 Web 应用安全工作组（Web Application Security Working Group）发布了 Referrer Policy 草案，对浏览器该如何发送 Referrer 做了详细的规定。新版 Chrome 已经支持了这份草案，我们终于可以灵活地控制自己网站的 Referrer 策略了。

但是！！！！！！！！从头信息中可以看到Referer-policy的字样，它的规则是： 
No Referrer：任何情况下都不发送 Referrer 信息；
No Referrer When Downgrade：仅当发生协议降级（如 HTTPS 页面引入 HTTP 资源，从 HTTPS 页面跳到 HTTP 等）时不发送 Referrer 信息。这个规则是现在大部分浏览器默认所采用的；
Origin Only：发送只包含 host 部分的 Referrer。启用这个规则，无论是否发生协议降级，无论是本站链接还是站外链接，都会发送 Referrer 信息，但是只包含协议 + host 部分（不包含具体的路径及参数等信息）；
Origin When Cross-origin：仅在发生跨域访问时发送只包含 host 的 Referrer，同域下还是完整的。它与 Origin Only 的区别是多判断了是否 Cross-origin。需要注意的是协议、域名和端口都一致，才会被浏览器认为是同域；
Unsafe URL：无论是否发生协议降级，无论是本站链接还是站外链接，统统都发送 Referrer 信息。正如其名，这是最宽松而最不安全的策略；

通过新的 Referrer Policy，我们可以针对第三方网站隐藏 Referrer，也可以只发送来源 URL 的 host 部分。但有一点要记住，新策略允许沉默，但不允许说谎。换句话说，你有权不告诉对方请求从哪儿来，但是不允许用假来源去骗人。不过即便是这样，这也对现有一些 Web 应用程序的安全性造成威胁。不少 Web 应用在限制 Referrer 时允许为空，之前想要发送无 Referrer 请求还要一点点技巧，现在就轻而易举了。
Referrer Policy States

一般网站的policy都是 no-referrer-when-downgrade。

referer的作用
由于referer是请求网页中，也就是发起HTTP请求中header的一部分，所以可以用来做网页的图片防盗链！** 
比如一个网页的图，想用python下载到自己的电脑里，用urllib.request或者requests第三方库访问图片时，爬不下来， 
这是因为python提交request申请的时候，就类似于在浏览器中的空地址栏里键入这个网页然后访问，根据上面说的，无referer，这时网站的设置比如是要求有referer，且referer的网站必须是你进来之前的网站，也就是这个图片的主页。

破解referer反爬虫的办法
方法很简单！ 既然要求你传入图片主页面的referer，在构造header的时候，传入Referer参数（注意R要大写），它的值为与这个图片链接相关的网站，或者这个图片链接地址的原网站就可以了.







