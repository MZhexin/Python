# 作者： 世界第一大帅哥
# 开发时间 2022/1/13 0:25

'''
   常见异常类型：
   1、ZeroDivisionError：除数为零（取模运算也算，且这个零可以是所有数据类型）
   2、IndexError：序列中没有此索引
   3、KeyError：映射中没有这个键
   4、NameError：未声明或未初始化对象（没有属性）
   5、SynatxError：Python语法错误
   6、ValueError：传入无效参数
'''

# try-except:
'''
   try:
      可能会出现异常的代码
   except 异常类型:
      报错后执行的代码
'''
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    c = a / b
    print('a除以b的结果为：', c)
except ZeroDivisionError:
    print('对不起，除数不能为零')
print('程序结束')

# try-except-else-finally:
'''
   try:
      可能会出现异常的代码
   except 异常类型:
      报错后执行的代码
   else:
      没有抛出异常时所执行的代码
'''
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    c = a / b
except BaseException as e:
    print('对不起，除数不能为零')
    print(e)
else:
    print('a除以b的结果为：', c)
print('程序结束')

# try-except-else:
'''
   try:
      可能会出现异常的代码
   except 异常类型:
      报错后执行的代码
   else:
      没有抛出异常时所执行的代码
   finally:
      无论如何都会执行的代码
'''
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    c = a / b
except BaseException as e:
    print('对不起，除数不能为零')
    print(e)
else:
    print('a除以b的结果为：', c)
finally:
    print('程序结束')
