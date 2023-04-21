# 作者： 世界第一大帅哥
# 开发时间 2022/1/4 20:16

# input()函数
# input()函数的输出结果是str类型（一定要记得转换成所需的类型）
present = input("大圣想要什么礼物呢？")
print(present, type(present))

# 读取两个整数并计算它们的和
# 方法一：
a = input("请输入第一个加数：")   # 先进行输入
a = int(a)    # 转换之后再存储在a中
b = input("请输入第二个加数：")   # 先进行输入
b = int(b)    # 转换之后再存储在b中
print(a+b)
# 方法二：
c = int(input("请输入第一个加数："))     # 将输入数字转换为整型之后再存储在c中
d = int(input("请输入第二个加数："))     # 将输入数字转换为整型之后再存储在d中
print(c+d)

