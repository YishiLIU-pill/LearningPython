#Python列表
print ("Welcome to List")
'''列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串
甚至可以包含列表（即嵌套）。
列表用[]标识，是python最通用的复合数据类型。
'''
#Python列表截取
t = ['a', 'b', 'c', 'd', 'e']
print (t)
print (t[1:3])#应为['b','c']
print (t[3:]) #从NO3开始应为['d','e']
print (t[:4]) #NO4之前的应为['a','b','c','d']
print (t[:])  #应为['a','b','c','d','e']

list = [ 'Lewis', '100+', 'dayday', 'up', 'have$$$']
tinylist = ['614','hahaha']

print (list)           #输出完整列表
print (list [0])       #Lewis
print (list [1:3])     #[ '100+', 'dayday']
print (list [2:])      #['dayday', 'up', 'have$$$']
print (tinylist * 2)   #输出列表两次
print (list + tinylist)#打印组合的列表