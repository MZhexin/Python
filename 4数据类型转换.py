# 作者： 世界第一大帅哥
# 开发时间 2022/1/4 19:26

# 数据类型转换
name = '张三'
age = 24
identity = '学生'
print(type(name), type(age))
print("我的名字是"+name+"。\n"+str(age)+"岁,是"+identity+"。")
# 不同数据类型之间用加号（+）进行连接
# age是整型，其他都是字符串类型，故需要用str()进行数据类型转换
# 函数格式： 需要转换成的类型（需要进行转换操作的变量名）
# 一共有三种转换函数：1、int() 2、float() 3、str()

# str()的一些应用
a = 114514
b = 233.233
c = False
print(type(a), str(a), type(str(a)))
print(type(b), str(b), type(str(b)))
print(type(c), str(c), type(str(c)))
# 也可以用引号来进行转换成str类型
d = str(123)
e = "456"
print(d, type(d))
print(e, type(e))

# int()的一些应用
# 注意事项：
# 1、将str类型转换为int类型，str必须为整数串（小数串和非数字串都不行）
# 2、将float类型转换为int类型，直接取整（保留整数部分，舍弃小数部分）
# 3、将bool类型转换为int类型，True转为1，False转为0
f = "128"
g = 77.11
h = True
print(type(f), int(f), type(int(f)))
print(type(g), int(g), type(int(g)))
print(type(h), int(h), type(int(h)))

# float()的一些应用
# 若字符串为非数字串（数字串包括整数串与小数串），则不允许转换
i = "98.98"
j = "76"
k = True
l = 81
print(type(i), float(i), type(float(i)))
print(type(j), float(j), type(float(j)))
print(type(k), float(k), type(float(k)))
print(type(l), float(l), type(float(l)))


