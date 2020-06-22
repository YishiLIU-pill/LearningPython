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

#与Python字符串不一样的是，列表中的元素是可以改变的：
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = []
print(a)

#Python列表截取可以接受第三个参数，参数作用是截取的步长
letters = ['L', 'e', 'w', 'i', 's', 'o']
print(letters[1:4:2])

#逆向读取
def reverseWords(input):

#通过空格将字符串分隔符，把各个单词分割为列表
    inputWords = input.split(" ")
    
    #第一个参数-1表示最后一个元素
    #第二个参数为空表示移动到列表末尾
    #第三个参数为步长，-1表示逆向
    inputWords = inputWords[-1::-1]
    
    #重新组合字符串
    output = ' '.join(inputWords)
    return output

if __name__ == "__main__":
    input = 'LongLong like SS'
    rw = reverseWords(input)
    print(rw)

    
