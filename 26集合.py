# 作者： 世界第一大帅哥
# 开发时间 2022/1/11 22:13
# 集合

# 什么是集合？
# 属于可变类型的序列
# Python语言提供的内置数据结构
# 集合可以理解为没有value的字典

# 集合的创建
# 1、直接用花括号
s = {2, 3, 4, 5, 6, 'Hello'}   # 集合中禁止有重复的元素
print(s)
# 2、利用set()函数：将其他类型的数据转换成集合形式，并删去重复的元素
s1 = set(range(6))
s2 = set([3, 4, 53, 56])
s3 = set((3, 4, 43, 435))
s4 = set('Python')
s5 = set({124, 3, 4, 4, 5})
s6 = set()
print(type(s1), s1)
print(type(s2), s2)
print(type(s3), s3)
print(type(s4), s4)
print(type(s5), s5)
print(type(s6), s6)

# 集合元素的判断操作：in和not in
s = {10, 20, 30, 40}
print(10 in s)         # True
print(10 not in s)     # False
print(100 in s)        # False
print(100 not in s)    # True

# 集合的添加
s = {10, 20, 30, 40}
s.add(80)
print(s)
s.update([200, 100, 300])   # .update()函数可以往集合中添加集合、列表或元组，但一次至少添加一个元素
print(s)

# 集合元素的删除操作
# 1、remove()方法：一次删除一个指定元素（若该元素不存在，抛出异常）
s = {10, 20, 30, 40}
print('删除前：', s)
s.remove(10)
print('删除后：', s)
# 2、discard()方法：一次删除一个指定元素（若该元素不存在，不抛出异常）
s = {10, 20, 30, 40}
print('删除前：', s)
s.discard(10)
print('删除后：', s)
# 3、pop()方法：一次只删除一个任意元素
s = {10, 20, 30, 40}
print('删除前：', s)
s.pop()
print('删除后：', s)
# 4、clear()方法：清空集合
s = {10, 20, 30, 40}
print('删除前：', s)
s.clear()
print('删除后：', s)    # 结果为set()

# 集合间的关系
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
s4 = {90, 10, 20}
s5 = {70, 80, 90}
# 用==和!=判断两集合是否相等（即是否含有相同元素，且元素顺序不重要）
print(s3 == s4)    # True
print(s3 != s4)    # False
# .issubset()：判断一个集合是否是另一个集合的子集
print(s2.issubset(s1))    # True
print(s3.issubset(s1))    # False
# .issuperset()：判断一个集合是否是另一个集合的超集
print(s1.issuperset(s2))    # True
print(s1.issuperset(s3))    # False
# .isdisjoint()：判断两个集合是否有交集（结果的布尔值与事实容易混淆）
print(s1.isdisjoint(s3))    # False ——————> 表示有交集
print(s1.isdisjoint(s5))    # True ——————> 表示没有交集

# 集合的数学操作
# 1、.intersection()：找交集
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.intersection(s2))
print(s1 & s2)   # &操作等价于.intersection()操作
# 2、.union()：找并集
s1 = {10, 20, 30, 40}
s2 = {'您好', '再见', '拜拜了您嘞'}
print(s1.union(s2))
print(s1 | s2)   # |操作等价于.union()操作
# 3、.symmetric_difference()：找差集（并集-交集）
s1 = {20, 30, 40, 100}
s2 = {20, 30, 40, '您好', '再见'}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)   # ^操作等价于.symmetric_difference()操作 ————> 同时按住Shift和6的话可以打出^

# 集合生成式：将列表生成式的[]全部换成{}即可
# 语法格式：{i*i for i in range(1,10)}
s = [i for i in range(1, 10)]
print(s)
s = [i*i for i in range(1, 10)]
print(s)
