# 作者： 世界第一大帅哥
# 开发时间 2022/1/10 23:46

# 练习题：输出100到999之间的水仙花数
for i in range(100, 1000):
    ind = i // 100               # 个位的英文：individual
    ten = i // 10 % 10           # 十位的英文：ten
    hun = i % 10                 # 百位的英文：hundred
    if ind ** 3 + ten ** 3 + hun ** 3 == i:
        print(i)

# 水仙花数共有4个：153、370、371和407
