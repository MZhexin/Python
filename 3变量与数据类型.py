# 作者： 世界第一大帅哥
# 开发时间 2022/1/4 17:38


# 变量
name="世界第一大帅哥"
print("标识", id(name))     # 标识某种程度上可以理解为地址，这涉及到python建立一个新变量的原理，不展开叙述
print("类型", type(name))
print("数值", name)


# 整型：可以表示为十进制、二进制、八进制和十六进制（系统默认十进制）
# 以十进制数字118为例
print("十进制", 118)
print("二进制", 0b01110110)   # 0b+二进制数字
print("八进制", 0o166)        # 0o+八进制数字
print("十六进制", 0x76)       # 0x+十六进制数字


# 浮点型：由于存储方式特殊，计算有不准确性（如下例）
# 这种不精确说白了就是二进制的底层问题
print(1.1+2.2)
# 解决办法：导入Decimal模块（本节课不用知道原理，后面会讲）
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))


# 布尔型
f1 = True
f2 = False
print(f1)
print(type(f1))
print(f2)
print(type(f2))
# 布尔型可以转化为整数计算（直接计算即可）
print(f1+1)   # 结果为2，即1+1的结果
print(f2+1)   # 结果为1，即0+1的结果


# 字符串类型
# 单引号或双引号定义的字符串必须写在同一行
str1 = 'I am handsome.'
str2 = "You are ugly.\n"
# 三引号定义的字符串可以分布在连续多行（但不能用转义字符换行）
str3 = '''I\'m handsome.
          You are ugly.
          Megatron must be stopped.
          No matter the cost.'''
print(str1, str2, str3)
print(type(str1), type(str2), type(str3))
