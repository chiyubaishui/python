3.0 Django框架
3.0.1 MVC框架和MTV框架
	MVC，全名是Model View Controller，是软件工程中的一种软件架构模式，把软件系统分为三个基本部分：模型(Model)、视图(View)和控制器(Controller)，具有耦合性低、重用性高、生命周期成本低等优点。
	Django框架的不同之处在于它拆分的三部分为：Model（模型）、Template（模板）和View（视图），也就是MTV框架。
	Model(模型)：负责业务对象与数据库的对象(ORM)
	Template(模版)：负责如何把页面展示给用户
	View(视图)：负责业务逻辑，并在适当的时候调用Model和Template
