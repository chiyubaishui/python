# p = Pool()
# p.map(funcname,iterable)     默认异步的执行任务,且自带close和join
# p.apply   同步调用的
# p.apply_async 异步调用 和主进程完全异步 需要手动close 和 join
# from multiprocessing import Pool
# def func(i):
#     return i*i
#
# if __name__ == '__main__':
#     p = Pool(5)
#     for i in range(10):
#         res = p.apply(func,args=(i,))   # apply的结果就是func的返回值
#         print(res)

# import time
# from multiprocessing import Pool
# def func(i):
#     time.sleep(0.5)
#     return i*i
#
# if __name__ == '__main__':
#     p = Pool(5)
#     res_l = []
#     for i in range(10):
#         res = p.apply_async(func,args=(i,))   # apply的结果就是func的返回值
#         res_l.append(res)
#     for res in res_l:print(res.get())# 等着 func的计算结果

# import time
# from multiprocessing import Pool
# def func(i):
#     time.sleep(0.5)
#     return i*i
#
# if __name__ == '__main__':
#     p = Pool(5)
#     ret = p.map(func,range(100))
#     print(ret)
