print(" Welcome to tuple ")
'''元组是另一个数据类型，类似于List(列表）。
元组用()标识，内部元素用逗号隔开，但是元组不能二次赋值，相当于只读列表。
'''

tuple = ( 'Lewis', 'like', '100+', '$$$', 'eateateat')
tinytuple = (614, 'Lewis')

print (tuple)
print (tuple[0])          #Lewis
print (tuple[1:3])        #('like','100+')
print (tuple[2:])         #('100+','$$$','eateateat')
print (tinytuple * 2)     #tinytuple_twice
print (tuple + tinytuple) #打印组合的元组

'''
>>> tup = (1, 2, 3, 4, 5, 6)
>>> print(tup[0])
1
>>> print(tup[1:5])
(2, 3, 4, 5)
>>> tup[0] = 11  # 修改元组元素的操作是非法的
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
'''
#虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表
#构造包含0个或1个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = () #空元组
tup2 = (20,)#一个元素，需要在元素后添加逗号
print(tup1,tup2)

#String, list和tuple都属于sequence(序列)