# 作者： 世界第一大帅哥
# 开发时间 2022/1/4 20:56

# 赋值运算符计算方向：从右到左
i = 3+4     # 先计算出3+4=7，再把7赋值给i
print(i)

# 支持链式赋值
A = B = C = 20
print(A, id(A))
print(B, id(B))
print(C, id(C))
# ABC的值一样，id（地址）也都一样

# 支持参数赋值
a = 10
print(a, type(a))
a += 10
print(a, type(a))
a -= 10
print(a, type(a))
a *= 10
print(a, type(a))
a /= 10
print(a, type(a))
a //= 10
print(a, type(a))
a %= 10
print(a, type(a))

# 支持系列解包赋值
X, Y, Z = 10, 20, 30
print(X, Y, Z)
# 系列解包赋值的应用:可以用来快速交换x和y的值（无需中间变量）
x, y = 10, 20
print("交换之前：", "x="+str(x), "y="+str(y))
x, y = y, x
print("交换之后：", "x="+str(x), "y="+str(y))
