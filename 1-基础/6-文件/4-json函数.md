1、json.dumps()
    json.dumps()用于将dict类型的数据转成str，因为如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到该函数。

import json
name_emb = {'a':'1111','b':'2222','c':'3333','d':'4444'} 
jsObj = json.dumps(name_emb)    
print(name_emb)
print(jsObj)
print(type(name_emb))
print(type(jsObj))
运行结果如下：
{'a': '1111', 'c': '3333', 'b': '2222', 'd': '4444'}
{"a": "1111", "c": "3333", "b": "2222", "d": "4444"}
<type 'dict'>
<type 'str'>

若在数据写入json文件时，未先进行转换，报错如下
import json  
name_emb = {'a':'1111','b':'2222','c':'3333','d':'4444'}          
emb_filename = ('/home/cqh/faceData/emb_json.json')   
# jsObj = json.dumps(name_emb)     
with open(emb_filename, "w") as f:  
    f.write(name_emb)  
    f.close()  

2、json.loads()
	json.loads()用于将str类型的数据转成dict。	
import json
name_emb = {'a':'1111','b':'2222','c':'3333','d':'4444'} 
jsDumps = json.dumps(name_emb)    
jsLoads = json.loads(jsDumps) 
print(name_emb)
print(jsDumps)
print(jsLoads)
print(type(name_emb))
print(type(jsDumps))
print(type(jsLoads))     

运行结果如下：'a'变成了u'a'是因为发生了类型转换，str会转换成unicode
{'a': '1111', 'c': '3333', 'b': '2222', 'd': '4444'}
{"a": "1111", "c": "3333", "b": "2222", "d": "4444"}
{u'a': u'1111', u'c': u'3333', u'b': u'2222', u'd': u'4444'}
<type 'dict'>
<type 'str'>
<type 'dict'>

3、json.dump()
	json.dump()用于将dict类型的数据转成str，并写入到json文件中。下面两种方法都可以将数据写入json文件

import json   
name_emb = {'a':'1111','b':'2222','c':'3333','d':'4444'}            
emb_filename = ('/home/cqh/faceData/emb_json.json')  
# solution 1
jsObj = json.dumps(name_emb)    
with open(emb_filename, "w") as f:  
    f.write(jsObj)  
    f.close()      
# solution 2   
json.dump(name_emb, open(emb_filename, "w"))

4、json.load()
	json.load()用于从json文件中读取数据。

import json  
emb_filename = ('/home/cqh/faceData/emb_json.json')  
jsObj = json.load(open(emb_filename))    
print(jsObj)
print(type(jsObj))
for key in jsObj.keys():
    print('key: %s   value: %s' % (key,jsObj.get(key)))
 
运行结果如下：
{u'a': u'1111', u'c': u'3333', u'b': u'2222', u'd': u'4444'}
<type 'dict'>
key: a   value: 1111
key: c   value: 3333
key: b   value: 2222
key: d   value: 4444
