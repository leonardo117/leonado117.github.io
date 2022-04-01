from msilib.schema import Class
from operator import truediv


'''
python语法用缩进代表代码块{}
'''
if True:
    print("1")
else:
    print("2")


'''
多行语句
\
'''
i = 1 + \
    2 + \
    3
print(i)


"""
模块
"""
#import sys
#for i in sys.argv:
#    print(i)
#print('\n path:', sys.path)
'''
from sys import argv, path
for i in argv:
    print(i)
print("参数列表", str(argv))
'''
import keyword
#keyword.kwlist
print(str(keyword.kwlist))

#包概念
#_init_.py目录下包含此文件将视作包
#from xx.xx import xx  #进行模块的引入


'''
数据类型
'''
# 赋值
a=a1=a2=1
a, b, c = 1, 1.0, '字符串'

'''
可变数据类型:List, Dictionary, Set
不可变数据类型:Number, String, Tuple
'''
'''
Number
'''
n = True
b1 = type(n) == int
b2 = type(n) == bool
b3 = isinstance(n, int)
b4 = isinstance(n, bool)
b5 = issubclass(bool, int)
print('数据类型:', b1, b2, b3, b4, b5)
del b1, b2

c = 1/2
c1 = 1//2
print(c, c1)

print(7%3)
print(2**3)

# 复数
c = 1 + 2j; c1 = complex(1, 2)

'''
String
'''
str1 = "我是转义符\n"
str2 = r"我是转义符\n" 
print(str1)
print(str2)

# python语法中""和''相同，所以没有字符意义，只有字符串

str3 = '123456789'
print(str3[1::2])
print(str3[0:-1])
print(str3[0:-2])
print((str3 + '叠加') * 2)
print(str3 + '不换行', end=" ");print(str3)
print('观察叠加参数效果', str1, str2, str3)


'''
List
'''
list = [ 'abcd', 786 , 2.23, '重复测试', 70.2 ]
tinylist = [123, '重复测试']

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

l = [1, 2, 3, 4, 5, 6]
print(l[2:5])
l[2:5] = []             # 修改
print(l)

'''
Tuple(元组)
'''
t = (1, "测试", 1.0)
# t[0] = 2 元组不可修改
t1 = (l, 1, t)
print(t1)

'''
Set(集合)
'''
s = {'测试', 1, 1.0, 1}
print(s)
#集合运算
a = set('dfadfmmi')
b = set('sdfaprto')
print(a)
print(a - b) #差集
print(a | b) #并集
print(a & b) #交集
print(a ^ b) #不同时存在集合

'''
Dictionary(字典)
'''
tmpDic = {'cs':'dd', 'po':'fd', 'cs':1}
print(tmpDic)

dic = {}
dic['测试'] = 1
dic[2] = 'value'
print(dic)
print(dic.keys())
print(dic.values())

'''
数据类型的转换
显式：str(), int()等
隐式：向高级别转，防止数据丢失
'''

'''
推导式
'''
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper() for name in names if len(name)>3]
print(new_names)

dic = {x: x**2 for x in (2, 4, 6)}
print(dic)
set = {x**2 for x in (2, 4, 6)}
print(set)
tup = (x**2 for x in (2, 4, 6))
print(tup) #生成器对象
print(tuple(tup))

'''
迭代器
'''
L = [1, 2, 3]
it = iter(L)
print(next(it))

'''
生成器
'''

'''
函数
'''
def sm():
    print('我是一个函数')
sm()

def printinfo(*info):
    print(info)
    for i in info:
        print(i)
    #return
printinfo(1, 3, 4)

def printdic(**info):
    print(info)
#printdic(2,1)
printdic(a=2, b=1)

#强制位置参数
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
f(1, 2, 3, d=4, e=5, f=6)


'''
lambda
'''
# lambda求和
sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))


'''
类
'''
#以下self并非关键字，换成其他命名也可运行
class MyClass:
    #基本属性
    m = 1
    #私有属性,两下划线开头
    __mp = 0
    #构造函数
    def __init__(self):
        self.a = 0
        self.b = False
    #def mf():
    def mf(self):
        return '我是MyClass类下的mf函数'
c = MyClass()
print(c.m, c.a, c.b)
print('说明',c.mf())

#单继承
class son(MyClass):
    son_m = 1

#多态
class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')
 
class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法

'''
作用域
'''
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print(num)
fun1()
print(num)

def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()