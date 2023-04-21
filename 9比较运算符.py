# 作者： 世界第一大帅哥
# 开发时间 2022/1/7 0:01

# 比较运算符的运行结果为bool类型
a = int(input("请输入a的值："))
b = int(input("请输入b的值："))
print(a, b)
print("a大于b吗？", a > b)
print("a小于b吗？", a < b)
print("a等于b吗？", a == b)
print("a不等于b吗？", a != b)
print("a大于等于b吗？", a >= b)
print("a小于等于b吗？", a <= b)


'''
   一个变量由三个部分组成：标识（id）、类型、值
   ==比较的是变量的值
   若想比较变量的标识，需要使用 is 和 is not
   
   is：表示两个变量id相等
   is not：表示两个变量的id不相等
'''
x = 10
y = 10
print(x == y)     # 结果为True，表示x和y的值是一样的
print(x is y)     # 结果为True，表示x和y的id是一样的
# 以下代码没有学过，先这样写，后面会有讲解
list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)   # 结果为True
print(list1 is list2)   # 结果为False
print(id(list1))
print(id(list2))
print(x is not y)            # 结果为False
print(list1 is not list2)    # 结果为True
