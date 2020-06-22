print("Welcome to base grammar!")
#多行语句
#Python通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句

total = 'Lewis Liu ' \
        'is ' \
        'a ' \
        'magic witch!'
print (total)

#数字(Number)类型
'''
python中数字有四种类型:整数, 布尔型, 浮点数和复数。
int, 如1,只有一种整数类型int, 表示长整型
bool, 如true
float, 如1.23, 3E-2
complex, 如1 + 2j, 1.1 + 2.2j
'''

#字符串(String)
word = '字符串'
sentence = "这是一个句子"
paragraph = """ 
                这是一个段落
                我爱薯条
                薯条爱我
            """
print (word)
print (sentence)
print (paragraph)

'''
转义符'\'
反斜杠可以用来转义，使用r可以让反斜杠不发生转义，
如：r"this is a line with\n" 则\n会显示，并不是换行
'''
print ('hello\nrunoob')# 使用反斜杠(\)+n转义特殊字符
print (r'hello\nrunoob')# 在字符串前面添加一个r，表示原始字符串，不会发生转义

#等待用户输入
input("\n\n按下 enter 键后退出。")
#以上代码\n\n在结果输出前会输出两个新的空行。一旦用户按下enter键时，程序将退出。

#同一行显示多条语句
'''
Python可以在同一行中使用多条语句，
语句之间使用分号(;)分割
'''
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

#多个语句构成代码组
'''
缩进相同的一组语句构成一个代码块，我们称之为代码组
像if, while, def和class这样的复合语句，首行以关键字开始，以冒号(:)结束，
该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。

if expression :
    suite
elif expression :
    suite
else :
    suite
'''

#Print输出
'''
print默认输出是换行的，如果要实现不换行需要在变量末尾加上end=""
'''
x = "a"
y = "b"
# 换行输出
print (x)
print (y)

print ('------------')
#不换行输出
print (x, end=" ")
print (y, end=" ")
print ( )

#import与from...import
'''
在python用 import 或者 from...import 来导入相应的模块
将整个模块(somemodule)导入，格式为：import somemodule
从某个模块中导入某个函数，格式为：from somemodule import somefunction
从某个模块中导入多个函数，格式为：from somemodule import firstfunc,
sencondfunc, thirdfunc
将某个模块中的全部函数导入，格式为：from somemodule import *
'''
#导入sys模块
import sys
print('==========Python import mode==========')
print('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为', sys.path)

#导入sys模块的argv,path成员
from sys import argv,path #导入特定的成员

print('==========python from import==========')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path