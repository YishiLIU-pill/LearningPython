print("Welcome to for loop statement!")
# Python for 循环语句
'''语法：
for循环的语法格式如下：
for iterating_var in sequence:
    statements(s)
    系列中的元素->代码块(statement)->返回系列中的元素
                ->输出    
'''
for letter in 'Python':  #第一个实例
    print('当前字母:',letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:     #第二个实例
    print('当前水果：',fruit)

print("Good bye!")

#通过序列索引迭代
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):#range()返回一个序列的数
    print('当前水果：', fruits[index])
print("Good bye!")

#循环使用else语句
for num in range(10,20):   #迭代10到20之间的数字
    for i in range(2,num): #根据因子迭代
        if num%i == 0:     #确定第一个因子
            j=num/i        #计算第二个因子
            print('%d等于%d*%d'%(num,i,j))
            break
    else:
        print(num,'是一个质数')