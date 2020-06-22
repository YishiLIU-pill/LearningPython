print("Welcome to Set!")
#Set (集合)
'''
集合(set)是由一个或数个形态各异的大小整体组成的
构成集合的事物或对象称作元素或是成员
基本功能是进行成员关系测试和删除重复元素
可以使用大括号{}或set()函数创建集合
注意：创建一个空集合必须用set()而不是{}，
因为{}是用来创建一个空字典
创建格式：
pareme = {value01, value02, ...}
或者
set(value)
'''

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites) #输出集合，重复的元素被自动去掉

#成员测试
if 'Runoob' in sites :
    print('Runoob在集合中')
else :
    print('Runoob不在集合中')

#set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(b)

print(a - b)    #a 和 b的差集

print(a | b)    #a 和 b的并集

print(a & b)    #a 和 b的交集

print(a ^ b)    #a 和 b中不同时存在的元素

