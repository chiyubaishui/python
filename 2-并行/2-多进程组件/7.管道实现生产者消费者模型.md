# from multiprocessing import Lock,Pipe,Process
# def producer(con,pro,name,food):
#     con.close()
#     for i in range(100):
#         f = '%s生产%s%s'%(name,food,i)
#         print(f)
#         pro.send(f)
#     pro.send(None)
#     pro.send(None)
#     pro.send(None)
#     pro.close()
#
# def consumer(con,pro,name,lock):
#     pro.close()
#     while True:
#             lock.acquire()
#             food = con.recv()
#             lock.release()
#             if food is None:
#                 con.close()
#                 break
#             print('%s吃了%s' % (name, food))
# if __name__ == '__main__':
#     con,pro = Pipe()
#     lock= Lock()
#     p = Process(target=producer,args=(con,pro,'egon','泔水'))
#     c1 = Process(target=consumer, args=(con, pro, 'alex',lock))
#     c2 = Process(target=consumer, args=(con, pro, 'bossjin',lock))
#     c3 = Process(target=consumer, args=(con, pro, 'wusir',lock))
#     c1.start()
#     c2.start()
#     c3.start()
#     p.start()
#     con.close()
#     pro.close()

# from multiprocessing import Process,Pipe,Lock
#
# def consumer(produce, consume,name,lock):
#     produce.close()
#     while True:
#         lock.acquire()
#         baozi=consume.recv()
#         lock.release()
#         if baozi:
#             print('%s 收到包子:%s' %(name,baozi))
#         else:
#             consume.close()
#             break
#
# def producer(produce, consume,n):
#     consume.close()
#     for i in range(n):
#         produce.send(i)
#     produce.send(None)
#     produce.send(None)
#     produce.close()
#
# if __name__ == '__main__':
#     produce,consume=Pipe()
#     lock = Lock()
#     c1=Process(target=consumer,args=(produce,consume,'c1',lock))
#     c2=Process(target=consumer,args=(produce,consume,'c2',lock))
#     p1=Process(target=producer,args=(produce,consume,30))
#     c1.start()
#     c2.start()
#     p1.start()
#     produce.close()
#     consume.close()

# pipe 数据不安全性
# IPC
# 加锁来控制操作管道的行为 来避免进程之间争抢数据造成的数据不安全现象

# 队列 进程之间数据安全的
# 管道 + 锁
