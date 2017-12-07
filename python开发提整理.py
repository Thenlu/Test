'''
#1输出1-100 的和？第一种
print(sum(range(101)))

#1输出1-100 的和？第二种
# a = reduce(lambda a,b :a+b,range(1,101))

#1输出1-100 的和？第三种
n = 0
for i in range(1,101):
    n = n + i
print(n)

#删除重复元素？
li = [1,2,3,4,5,5,6,6,7,88,998,1]
b = set(li)
print(b)

#实现字符串，整数，浮点数之间的转换？
k = "56"
print(type(k))
s= int(k)
print(type(s))
s= float(k)
print(type(s))
'''
#实现u'中国'与’中国‘的互相转化
# a = u'中国'
# print(a.encode())
# b = '\xe4\xb8\xad\xe5\x9b\xbd'
# print(b.unicode)

#解释下面的代码
print([1,2,3,'b'][6:]) #其中的6 代表这第一个列表的数，第一个列表没有6的数所以获取不到

