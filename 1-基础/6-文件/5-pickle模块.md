pickle模块介绍
pickle模块实现了用于序列化和反序列化python对象结构的二进制协议。 序列化操作"pickling"是将python对象层次结构转换为字节流的过程，反序列化操作 "unpickling"则是将字节流转换回对象层次结构。
不得不提到的是，pickle是python所独有的，因此非python程序可能无法重构pickle对象。在工作中，我就遇到一个问题，就是我用sklearn训练得到的机器学习模型，用pickle保存下来后，工程方面的同事是没法用java调用这个模型的，一个临时的方法是有位同事读pickle源码，自己用java一步步反序列化回来，佩服佩服。
pickle使用技巧
对于最简单的代码，使用 dump() 和 load() 函数便足够了。

import pickle
a = 1

# 保存
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# 读取
with open('data.pickle', 'rb') as f:
    b = pickle.load(f)