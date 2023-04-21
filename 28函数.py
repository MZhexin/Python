# 作者： 世界第一大帅哥
# 开发时间 2022/1/13 0:05
'''
    def 函数名([参数]):
        函数体
        return 返回值
'''
def calculation(a, b) :
    c = b - a
    return c
answer = calculation(10, 20)
result = calculation(b=20, a=10)
print(answer)    # 结果为10
print(result)    # 结果为10
# 上述两种写法是一样的

# 函数的参数
def function1(a, b=3):      # 默认了形式参数b的值为3
    c = a + b
    return c
answer = function1(5)       # 输入a的值为5，默认b的值为3，返回c的值为5+3=8
result = function1(5, 5)    # 输入a的值为5，改变b的值为3，返回c的值为5+5=10
print(answer)    # 结果为8
print(result)    # 结果为10

# 个数可变的形参：
# 1、个数可变的位置参数
# 用于无法事先确定的传递的位置实参的个数时
# 用*定义个数可变的位置形参
# 结果为一个元组
'''
   def 函数名（*参数名）:
       函数体
       return 返回值
   函数名（实参）
'''
def fun1(*parameter):    # “参数”的英文是"parameter"哦
    print(parameter)
fun1(10)
fun1(10, 20)
fun1(10, 20, 30)
# 2、个数可变的关键字参数
# 用于无法事先确定的传递的关键字实参的个数时
# 用**定义个数可变的关键字形参
# 结果为一个字典
'''
   def 函数名（**参数名）:
       函数体
       return 返回值
   函数名(关键字=实参)
'''
def fun2(**parameter):
    print(parameter)
fun2(a=10)
fun2(a=10, b=20)
fun2(a=10, b=20, c=30)

# 在函数内部声明的变量是局部变量
# 局部变量用global声明，就变成了全局变量
def fun3():
    global age1    # 将age1变成全局变量
    age1 = 10
    print(age1)
fun3()           # 结果为10
print(age1)      # 结果为10
