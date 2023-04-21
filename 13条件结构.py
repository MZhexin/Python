# 作者： 世界第一大帅哥
# 开发时间 2022/1/7 18:11

# 条件结构
a = int(input('请输入一个数字：'))
if a > 0:
    if a % 2 == 0:
        print('这是一个正偶数。')
    else:
        print('这是一个正奇数。')
elif a < 0:
    if a % 2 == 0:
        print('这是一个负偶数。')
    else:
        print('这是一个负奇数。')
else:
    print('这是零。')

# 条件表达式：
# x if 判断条件 else y
# 如果判断条件的布尔值为True，运行表达式x，否则运行表达式y
# 例子：比较两个键入整数的大小
num_a = int(input('请输入第一个整数：'))
num_b = int(input('请输入第二个整数：'))
print(str(num_a)+'大于等于'+str(num_b) if num_a >= num_b else str(num_a)+'小于等于'+str(num_b))
