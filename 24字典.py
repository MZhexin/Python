# 作者： 世界第一大帅哥
# 开发时间 2022/1/11 9:51
# 字典

# 什么是字典？
# Python内置的数据结构之一，与列表一样是一个可变序列
# 以键值对的方式储存数据（e.g.'张三':100 ——> '张三'是键，100是值，'张三':100是键值对）
# 字典中键不可重复，但值可以重复
# 键可以是整数、浮点、字符串或布尔值
# 字典是一个无序的序列

# 字典的实现原理（与现实生活中的查字典类似）：
# 查字典是根据部首或拼音查找相应的页码
# Python中的字典是根据键（key）查找值（value）所在的位置

# 字典的创建：
# 1、使用花括号（最常用方式）
scores = {'张三': 100, '李四': 98, '王二麻子': 45}
print(scores)
print(type(scores))
# 2、使用内置函数dict() ——>dict是字典dictionary的缩写
# 由于是赋值的形式，等号左侧的变量名不用加引号；等号右侧是否加引号取决于数据类型
student = dict(name='田所浩二', age=24)
print(student)      # 结果为{'name': '田所浩二', 'age': 24} ——> 打印时自动修正为花括号形式
# 3、创建空字典
d0 = {}
print(d0)    # 结果为{}

# 获取字典中的元素
d1 = {'张三': 100, '李四': 98, '王二麻子': 45}
# 第一种方式：使用[]————>通过 字典名[键名] 获取该键对应的值
# 如果给定的键名不存在，会报错（KeyError）
print(d1['张三'])
# 第二种方式：使用get()————>通过 字典名.get(键名) 获取该键对应的值
# 如果给定的键名不存在，不会报错，但会打印None
# 如果给定的键名不存在，且在该键名后加上一个值，会打印加上的值
print(d1.get('张三'))
print(d1.get('你大爷'))           # 结果为None（d1中没有'你大爷'这个键名）
print(d1.get('你二爷', 144514))   # 结果为144514（d1中没有'你二爷'这个键名）

# 判断键是否在字典中（in和not in）
d2 = {'张三': 100, '李四': 98, '王二麻子': 45}
print('张三' in d2)          # 结果为True
print('张三' not in d2)      # 结果为False
print('孙悟空' in d2)        # 结果为False
print('孙悟空' not in d2)    # 结果为True

# 字典中键的删除
d3 = {'张三': 100, '李四': 98, '王二麻子': 45}
print('删除前：', d3)
del d3['张三']      # 删除指定的键值对（把键值对 '张三': 100 从字典d3中删除了）
print('删除后：', d3)

# 字典的清空
d4 = {'张三': 100, '李四': 98, '王二麻子': 45}
d4.clear()   # 清空字典d4，使其变为空字典
print(d4)

# 字典的增添与修改
d5 = {'张三': 100, '李四': 98, '王二麻子': 45}
print('增添前：', d5)
d5['野兽先辈'] = 1919810     # 增添键值对 '野兽先辈':1919810
print('增添后：', d5)
d5['野兽先辈'] = 114514      # 修改原键值对 '野兽先辈':1919810 为新键值对 '野兽先辈':114514
print('修改后：', d5)

# 获取字典视图的三种方法
d6 = {'张三': 100, '李四': 98, '王二麻子': 45}
# 1、keys():获取字典中所有的键
keys = d6.keys()
print(keys)          # dict_keys(['张三', '李四', '王二麻子'])
print(type(keys))    # <class 'dict_keys'>
print(list(keys))    # ['张三', '李四', '王二麻子']  ——————>将所有的键转换为列表形式
# 2、values():获取字典中所有的值
values = d6.values()
print(values)          # dict_values([100, 98, 45])
print(type(values))    # <class 'dict_values'>
print(list(values))    # [100, 98, 45]
# 3、items():获取字典中所有的键值对
items = d6.items()
print(items)           # dict_items([('张三', 100), ('李四', 98), ('王二麻子', 45)])
print(type(items))     # <class 'dict_items'>
print(list(items))     # [('张三', 100), ('李四', 98), ('王二麻子', 45)]
# 最后这一行的所有结果构成的列表是由元组组成的（将在下一章节进行讲解）

# 字典元素的遍历
d7 = {'张三': 100, '李四': 98, '王二麻子': 45}
# 输出字典中所有的键
for item in d7:
    print(item)
# 输出字典中所有的值
# 方法一：
for item in d7:
    print(d7[item])
# 方法二：
for item in d7:
    print(d7.get(item))

'''
   字典的特点：
   1、字典中所有的元素都是键值对，键不允许重复，值允许重复；
   2、字典中的元素是无序的；
   3、字典中的key必须是不可变对象；
   4、字典可以根据需要动态地伸缩；
   5、字典会浪费较大的内存，是一种使用空间换时间的数据。
'''

# 字典生成式：
# {键的表达式：值的表达式 for 表示键的变量，表示值的变量 in zip(可迭代对象)}
items = ['Fruits', 'Books', 'Others']  # 构建一个表示商品名称的列表
prices = [96, 78, 85]  # 构建一个表示商品价格的列表
d = {item: price for item, price in zip(items, prices)}
print(d)
# .upper()可将键中的英文字母全部转为大写
d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
# 如果键和值的列表中元素个数不一致，则以个数少的为准
items1 = ['Fruits', 'Books', 'Others']
prices1 = [96, 78, 85, 100, 200]
d = {item: price for item, price in zip(items, prices)}
print(d)    # 结果为{'Fruits': 96, 'Books': 78, 'Others': 85} ————>与值列表中的100和200两个元素无关
