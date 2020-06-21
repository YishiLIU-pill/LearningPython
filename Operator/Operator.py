print("Welcome to Operator")
#Python 运算符
''' Python语言支持以下类型的运算符：
算术运算符
比较(关系)运算符
赋值运算符
逻辑运算符
位运算符
成员运算符
身份运算符
运算符优先级
'''
#a**b 为a的b次方 即a的b次幂
#取整除(向下取整)， 9//2 = 4， -9//2 = -5

a = 21
b = 10
c = 0

c = a + b
print("c 的值为：", c)
c = a - b 
print("c 的值为：", c)
c = a * b 
print("c 的值为：", c)
c = a / b 
print("c 的值为：", c)
c = a % b 
print("c 的值为：", c)
#修改变量a,b,c 
a = 2
b = 3
c = a ** b 
print("c 的值为：", c)
a = 10
b = 5
c = a // b 
print("c 的值为：", c)

#Python 比较运算符
'''
== 相等
!= 不相等
<> 不相等
>  大于
<  小于
>= 大于等于
<= 小于等于
'''

a = 21
b = 10
c = 0

if a == b :
    print ("a等于b")
else :
    print ("a不等于b")
if a != b :
    print ("a不等于b")
else :
    print ("a等于b")
if a < b :
    print ("a小于b")
else :
    print ("a大于等于b")
if a > b :
    print ("a大于b")
else :
    print ("a小于等于b")
 
# 修改变量a 和 b 的值
a = 5
b = 20
if a <= b :
    print ("a小于等于b")
else :
    print ("a大于b")
if b >= a :
    print ("b大于等于a")
else :
    print ("b小于a")

#Python 赋值运算符
'''
+=, c += a , c = c + a
-=, c -= a , c = c - a 
*=, c *= a , c = c * a 
/=, c /= a , c = c / a 
%=, c %= a , c = c % a 
**=, c **= a , c = c ** a
//=, c //= a , c = c // a 
'''
    
a = 21
b = 10
c = 0

c = a + b 
print ("c 的值为: ", c)

c += a
print ("c 的值为: ", c)

c *= a 
print ("c 的值为: ", c)

c /= a 
print ("c 的值为：", c)

c = 2
c %= a 
print ("c 的值为：", c)

c **= a 
print ("c 的值为：", c)

c //= a
print ("c 的值为：", c)

#Python 位运算符
'''
a = 0011 1100
b = 0000 1101
-----------------------
a&b = 0000 1100 (全1为1)
a|b = 0011 1101 (一半为1)
a^b = 0011 0001 (相异为1)
~a = 1100 0011  (取反) -a-1 = -61
<< 左移动运算符，运算数的各二进位全部左移若干位
>> 右移动运算符，运算数的各二进位全部右移若干位
'''

a = 60      # 60 = 0011 1100
b = 13      # 13 = 0000 1101
c = 0

c = a & b;  # 12 = 0000 1100
print ("c的值为：", c )

c = a ^ b;  # 49 = 0011 0001
print ("c的值为：", c )

c = ~a;     #-61 = 1100 0011
print ("c的值为：", c )

c = a << 2; #240 = 1111 0000
print ("c的值为：", c )

c = a >> 2; # 15 = 0000 1111
print ("c的值为：", c )

#Python 逻辑运算符
'''
 and 若x为False, x and y 返回False, 否则返回y的计算值。
 or 若x是非0， 返回x的值，否则返回y的计算值。
 not 若x为True, 返回False，若为False返回True.
'''
a = 10
b = 20
 
if a and b :
    print ("变量a和b都为true")
else :
    print ("变量a和b有一个不为true")
    
if a or b :
    print ("变量a和b都为true，或其中一个变量为true")
else :
    print ("变量a和b都不为true")
    
# 修改变量a的值
a = 0
if a and b:
    print ("变量a和b都为true")
else :
    print ("变量a和b有一个不为true")
 
if a or b :
    print ("变量a和b都为true，或其中一个变量为true")
else :
    print ("变量a和b都不为true")
 
if not( a and b ) :
    print ("变量a和b都为false, 或其中一个变量为false")
else :
    print ("变量a和b都为true")


# Python 成员运算符
'''
in 如果在指定的序列中找到值返回True, 否则返回False
not in 如果在指定的序列中没有找到值返回True, 否则返回False
'''

a = 10
b = 20
list = [1, 2, 3, 4, 5];

if ( a in list ):
    print ("变量a在给定的列表List中")
else:
    print ("变量a不在给定的列表List中")

if ( b not in list ):
    print ("变量b不在给定的列表List中")
else:
    print ("变量b在给定的列表List中")

# 修改变量a的值
a = 2
if ( a in list ):
    print ("变量a在给定的列表List中")
else:
    print ("变量a不在给定的列表List中")
    

# Python 身份运算符
'''
is 是判断两个标识符是不是引用自一个对象
is not 是判断两个标识符是不是引用自不同对象
'''

a = 20
b = 20

if ( a is b ):
    print("a和b有相同的标识")
else:
    print("a和b没有相同的标识")

if ( a is not b ):
    print("a和b没有相同的标识")
else:
    print("a和b有相同的标识")
    
# 修改变量b的值
b = 30
if ( a is b ):
    print("a和b有相同的标识")
else:
    print("a和b没有相同的标识")

if ( a is not b ):
    print("a和b没有相同的标识")
else:
    print("a和b有相同的标识")

'''
is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个(同一块内存空间), ==用于判断
引用变量的值是否相等
例子：
>>> a = [1, 2, 3]
>>> b = a
>>> b is a 
True
>>> b == a
True
>>> b = a[:]
>>> b is a
False
>>> b == a
True
'''
# Python 运算符优先级
'''

**       指数(最高优先级)
~+-      按位翻转, 一元加号和减号(最后两个的方法名为+@和-@)正负
*/%//
+-       加法减法
>> <<    
&        位'AND'
^|
<= < > >= 比较运算符
== !=  
=% =/ =// -= += *= **= 赋值运算符
is is not 身份运算符 
in not in 成员运算符   
not and or 逻辑运算符
'''

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d
print(e)

e = ((a + b) * c)/ d 
print(e)

e = (a + b) * (c / d)
print(e)

e = a + (b * c)/d 
print(e)
