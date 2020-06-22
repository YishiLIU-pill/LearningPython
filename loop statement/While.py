print("Welcome to While loop statement!")

#simple example
a = 1
while a < 10:
    print (a)
    a += 2

#complex example
numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0 : #numbers列表长度大于0
    number = numbers.pop() #将一个numbers里的数字pop到number中
    if(number % 2 == 0) : 
        even.append(number) #把number里的数字放入even列表
    else :
        odd.append(number) #把number里的数字放入odd列表
print ("even:",even[:])
print ("odd:",odd[:])

#example1
count = 0
while (count < 9):
    print('The count is', count)
    count = count + 1

print("Good bye!")

# continue 和 break 用法
#continue用于跳过该次循环
#break则是用于退出循环
#判断条件 还可以是一个常值，表示循环必定成立

i = 1
while i < 10:
    i += 1
    if i % 2 > 0: #非双数时跳过输出
        continue
    print(i)     #输出双数2,4,6,8,10

i = 1
while 1:        #循环条件为1必定成立
    print(i)     #输出1~10
    i += 1
    if i > 10:   #当i大于10时跳出循环
        break

# 无限循环
#example2

var = 1
while var == 1: # 该条件永远为true，循环将无限执行下去
    num = int(input("Enter a number  :"))
    print("You entered:", num)

print("Good bye!") # 以上的无限循环可以用CTRL+C来中断循环


#循环使用else语句
count = 0
while count < 5:
    print (count, "is less than 5")
    count = count + 1
else:
    print (count, "is not less than 5")

#简单语句组
'''
类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句
与while写在同一行
'''
flag = 1
while (flag): print('Given flag is really true!')
print("Good bye!")
