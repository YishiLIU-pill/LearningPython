print('Welcome to Basic data type!')
#Python基本数据类型
'''
Python中的变量不需要声明
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建
在Python中，变量就是变量，它没有类型
我们所说的"类型"是变量所指的内存中对象的类型
等号(=)用来给变量赋值
等号(=)运算符左边是一个变量名，右边是存储在变量中的值
'''
counter = 100        #整型变量
miles   = 1000.0     #浮点型变量
name    = "runoob"   #字符串

print (counter)
print (miles)
print (name)

#多个变量赋值
#Python允许你同时为多个变量赋值
a = b = c = 1 #创建一个整型对象，值为1，从后向前赋值，三个变量被赋予相同的数值
print(a,b,c)

#也可以为多个对象指定多个变量
a, b, c = 1, 2, "runoob"
print(a,b,c)

#标准数据类型
'''
不可变数据(3个): Number(数字), String(字符串), Tuple(元组);
可变数据(3个): List(列表), Dictionary(字典), Set(集合)。
'''

#Number
#支持int, float, bool, complex
#内置的type()函数可以用来查询变量所指的对象类型
a, b, c, d = 20, 5.5, True, 4+3j
print(a,type(a),b,type(b),c,type(c),d,type(d))

'''
#此外，还可以用isinstance来判断
a = 111
isinstance(a,int)
True


isinstance和type的区别在于:
type()不会认为子类是一种父类类型
isinstance()会认为子类是一种父类类型

class A:
    pass
class B(A):
    pass
isinstance(A(),A)
True
type(A()) == A
True
isinstance(B(),A)
True
type(B()) == A
False
'''

#当你指定一个值时，Number对象就会被创建：
var1 = 1
var2 = 10
print(var1,var2)
#也可以使用del语句删除一些对象引用
#del语句的语法是：
#del var1[,var2[,var3[...,varN]]]

#也可以使用del语句删除单个或多个对象，如：
#del var1
#del var_a, var_b

word = 'Python'
print(word[0],word[5])
print(word[-1],word[-6])
