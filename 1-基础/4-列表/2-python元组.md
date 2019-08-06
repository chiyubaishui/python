PYTHON 元组操作

元组简介：python元组（Tuple）与列表(List)类似,不同之处在于元组不可修改，元组使用小括号，列表使用方括号
元组特性：不可修改

创建元组，实例如下：
tup1 = ("hello","world","ni hao")
tup2 = ("1","2","3")
tup3 = "a","b","c"
tup4 = () #空元组

访问元组，实例如下：
tup1 = ("hello","world","ni hao")
tup2 = ("1","2","3")
print tup1[1]
print tup2[0:]
print tup2[1:2]
print tup2[-1]
实例输出结果：
1 'world'
2 ('1','2','3')
3 ('2',)
4 ('3')

修改元组：
元组元素因为不可修改，只能进行连接组合

a=(1,2,3)
b=(2,3,4)
a+b
输出结果：
(1, 2, 3, 2, 3, 4)
删除元组：

元组元素因为不可修改，故而只能删除整个元组

a=(1,2,3,4)
print a
del a
print a

元组运算：
1.迭代
tup = (1,2,3)
#迭代
for a in tup:
    print a

#判断元素是否存在
a = 3
if a in tup:
    print 'element %d is exist' %(a) 
else:
    print 'element %d is not exist' %(a)

复制
tup1 = tup*4

获取长度
len(tup)