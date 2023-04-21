# 作者： 世界第一大帅哥
# 开发时间 2022/1/4 17:01

# 转义字符
print("hello\nworld")        # \n表示换行

print("hello\tworld")        # \t表示制表，每一个制表位为4个格，是否重开一个新的制表位取决于\t前是否占满一个制表位
print("helloooo\tworld")

print("hello\rworld")        # 打印完hello之后用\r回车，从头开始打印world，使world覆盖掉hello

print("hello\bworld")        # \b表示退一格，把o退掉之后继续打印world

# 原字符：让字符串中所有\都不表示转义字符（在引号前加一个r）
print("hello\nworld")
print(r"hello\nworld")

# 注意事项：字符串的最后一个字符不能是反斜线（但可以是俩反斜线）
# 错误示范： print("helloworld\)
print("helloworld\\")