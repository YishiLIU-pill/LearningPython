counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "Lewis" # 字符串
 
print (counter)
print (miles)
print (name)

#多个变量赋值
a = b = c =1
d, e, f = 1, 2, "Lewis"

print (a, b, c, d, e, f)

'''标准数据类型
python 有五个标准的数据类型

Numbers (数字）
String (字符串）
List (列表）
Tuple (元组）
Dictionary (字典）
'''
#Python数字
Var1 = 1
Var2 = 10

print (Var1, Var2)

''' 也可以使用del语句删除一些对象的引用
del语句的语法是：
del Var1[,Var2[,Var3[....,VarN]]]]

可以通过使用del语句删除单个或多个对象的引用
例如：
del Var
del Var_a, Var_b
'''

#Python字符串
'''字符串或串（String)是由数字，字母，下划线组成的一串字符。
一般记为：
s = "a1a2...an"(n>=0)

0   1  2  3  4  5
-6 -5 -4 -3 -2 -1
'''

#从字符串中获取一段子字符串，使用[头下标：尾下标]但不包含尾下标的字符
s = 'abcdef'
print (s)
print (s[1:5])

str = 'Hello World!'
print (str)          #输出完整字符串
print (str[0])       #输出字符串中的NO1字符
print (str[2:5])     #输出3-6之间的字符串
print (str[2:])      #输出从NO3开始的字符串
print (str * 2)      #输出字符串两次
print (str + "TEST") #输出连接的字符串

#Python列表截取
#接下来截取索引1到4的位置并设置步长为2（间隔一个位置）来截取字符串
letters = ['q', 'w', 'e', 'r', 't', 'y', 'u']
print (letters)
print (letters[1:4:2]) #应为w和r
