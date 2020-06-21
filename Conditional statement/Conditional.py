print ("Welcome to Conditional statement!")
#Python 条件语句
'''
Python条件语句是通过一条或多条语句的执行结果(True or False)来决定执行的
代码块。
Python程序语言指定任何非0和非空(null)值为true, 0或null为false。
Python编程中if语句用于控制程序的执行。
'''
# if 基本用法
flag = False
name = 'mofashaonv'
if name == 'python':        # 判断变量是否为python
    flag = True             # 条件成立时设置标志为true
    print('Welcome boss')
else:
    print (name) 

'''
if 语句的判断条件可以用>, <, ==, >=, <=来表示其关系
当判断条件为多个值时，可以使用以下形式:

if 判断条件1:
    执行语句1...
    
elif 判断条件2:
    执行语句2...
    
elif 判断条件3:
    执行语句3...
    
else:
    执行语句4...
'''

num = 5
if num == 3:
    print ('boss')
elif num == 2:
    print ('user')
elif num == 1:
    print ('worker')
elif num < 0:
    print ('error')
else:
    print ('roadman')

'''由于python并不支持switch语句，所以多个条件判断，只能用elif来实现，
如果判断需要多个条件需同时判断时，可以使用or，表示两个条件有一个成立时
判断条件成功; 使用and时，表示只有两个条件同时成立的情况下，判断条件成功。
'''

# if 语句多个条件

num = 9
if num >= 0 and num <= 10:
    print('hello')

num = 10
if num < 0 or num > 10:
    print('hello')
else:
    print('undefine')

num = 8
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print('hello')
else:
    print('undefine')

#简单的语句组
var = 100
if ( var == 100 ): print ("变量var的值为100")
print ("Good bye!")
    