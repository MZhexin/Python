# 作者： 世界第一大帅哥
# 开发时间 2022/1/7 0:23

a, b = 1, 2

# 布尔运算符之and（并且运算符，可以理解为C语言中的&&）
print(a == 1 and b == 2)   # 结果为True     结论：True and True ------> True
print(a == 1 and b < 2)    # 结果为False    结论：True and False ------> False
print(a != 1 and b == 2)   # 结果为False    结论：False and True ------> False
print(a != 1 and b != 2)   # 结果为False    结论：False and False ------> False

# 布尔运算符之or（或者运算符，可以理解为C语言中的||）
print(a == 1 or b == 2)   # 结果为True     结论：True or True ------> True
print(a == 1 or b < 2)    # 结果为True     结论：True and False ------> True
print(a != 1 or b == 2)   # 结果为True     结论：False and True ------> True
print(a != 1 or b != 2)   # 结果为False    结论：False and False ------> False

# 布尔运算符之not（取反运算符，对bool类型的运算数进行取反操作，把True变成False，把False变成True）
f1 = True
f2 = False
print(f1, f2)
print(not f1, not f2)

# 布尔运算符之in和not in（判断一个字符串A是否在另一个字符串B中）
s = "Hello World!"
print("W" in s)        # True
print("K" in s)        # False
print("W" not in s)    # False
print("K" not in s)    # True

