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


