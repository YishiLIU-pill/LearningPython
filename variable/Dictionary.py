print(" Welcome to Dictionary ")
'''字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型，
列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于: 字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{}"标识， 字典由索引(key)和它对应的值value组成
'''

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'Lewis', 'code': 'AE86', 'dept': 'magic'}

print (dict['one'])
print (dict[2])
print (tinydict)
print (tinydict.keys())   #输出所有键
print (tinydict.values()) #输出所有值

'''
Python数据类型转换
int(x[,base])          将x转换为一个整数
long(x[,base])         将x转换为一个长整数
float(x)               将x转换到一个浮点数
complex(real[,imag])   创建一个复数
str(x)                 将x转换为字符串
repr(x)                将x转换为表达式字符串
eval(str)              用来计算在字符串中的有效Python表达式，并返回一个对象
tuple(s)               将序列x转换为一个元组
list(s)                将序列x转换为一个列表
set(s)                 转换为可变集合
dict(d)                创建一个字典，d必须是一个序列(key,value)元组
frozenset(s)           转换为不可变集合          
chr(x)                 将一个整数转换为一个字符
unichr(x)              将一个整数转换为一个Unicode字符
ord(x)                 将一个字符转换为它的整数值
hex(x)                 将一个整数转换为一个十六进制字符串
oct(x)                 将一个整数转换为一个八进制字符串
'''

'''构造函数dic()可以直接从键值对序列中构造字典如下：
dict([('Runoob', 1),('Google', 2),('Taobao',3)])
{'Runoob': 1, 'Google': 2, 'Taobao': 3}

{x: x**2 for x in (2,4,6)}
{2: 4, 4: 16, 6: 36}

dict(Runoob=1, Google=2, Taobao=3)
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
'''