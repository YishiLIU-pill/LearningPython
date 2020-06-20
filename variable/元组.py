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