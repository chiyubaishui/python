向server端传送数据，
有2中方法，1 是 通过url 地址， 2 是通过路径     

#向server端传参数方式
    #1，通过数据 http://127.0.0.1:8000/blog/?id=2
    #2, 通过路径  http://17.0.0.1:8000/blog/20
                        # url(r'blog/(\d{4})')