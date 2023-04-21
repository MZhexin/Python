# 作者： 世界第一大帅哥
# 开发时间 2022/1/11 22:31

# 字符串的驻留机制：遇到多个内容相同的不可变字符串时，仅保留一份拷贝，并将其地址付给这些变量
a = 'Python'
b = "Python"
c = '''Python'''
print(a, id(a))   # 结果为Python 2224321217776
print(b, id(b))   # 结果为Python 2224321217776
print(c, id(c))   # 结果为Python 2224321217776

# 字符串的查找工作
'''
   查找方法：
   1、index()：查找子串第一次出现的位置（若子串不存在，会报错）
   2、rindex()：查找子串最后一次出现的位置（若子串不存在，会报错）
   3、fin()：查找子串第一次出现的位置（若子串不存在，返回-1）
   4、rfind()：查找子串最后一次出现的位置（若子串不存在，返回-1）
'''
s = 'hello,hello'
print(s.index('lo'))   # 3
print(s.find('lo'))    # 3
print(s.rindex('lo'))  # 9
print(s.rfind('lo'))   # 9
print(s.find('K'))     # -1
print(s.rfind('K'))    # -1
# 一般来说，建议使用find和rfind，因为不会报错

'''
   大小写变换操作：
   1、upper()：把字符串中所有字符都变成大写字母
   2、lower()：把字符串中所有字符都变成小写字母
   3、swapcase()：把字符串中所有大写字母变成小写字母，所有小写字母变成大写字母
   4、capitalize()：把第一个字符转换为大写字母，其余转换为小写字母
   5、title()：把每个单词的第一个字符变成大写字母，其余变成小写字母
'''
s = 'yOu ArE ugLY I aM HaNdsOme'
print(s.upper())         # YOU ARE UGLY I AM HANDSOME
print(s.lower())         # you are ugly i am handsome
print(s.swapcase())      # YoU aRe UGly i Am hAnDSoME
print(s.capitalize())    # You are ugly i am handsome
print(s.title())         # You Are Ugly I Am Handsome
# 上述操作会生成新的字符串（id不一样了）

# 对齐操作（由于不方便呈现，输出结果不写在注释里了）
s = 'hello,python'
# 1、center()
# 居中对齐，第一个参数指定宽度，第二个参数指定填充符（第二个参数可以不写，默认为空格）
# 若指定宽度小于原字符串长度，则返回原字符串
print(s.center(20))
print(s.center(20, '—'))
# 2、ljust()
# 左对齐，第一个参数指定宽度，第二个参数指定填充符（第二个参数可以不写，默认为空格）
# 若指定宽度小于原字符串长度，则返回原字符串
print(s.ljust(20))
print(s.ljust(20, '—'))
# 3、rjust()
# 右对齐，第一个参数指定宽度，第二个参数指定填充符（第二个参数可以不写，默认为空格）
# 若指定宽度小于原字符串长度，则返回原字符串
print(s.rjust(20))
print(s.rjust(20, '—'))
# 4、zfill()
# 右对齐，左边用0填充，只接收一个参数，用于指定宽度
# 若指定宽度小于原字符串长度，则返回原字符串
print(s.zfill(20))

# 字符串的劈分：
s1 = 'hello world python'
s2 = 'hello|world|python'
# 1、split()
# 从字符串左边部分开始劈分，默认的劈分字符是空字符串，返回的值都是一个列表
# 以参数sep指定劈分字符串的是劈分符
# 通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大劈分次数之后，剩余的子串会单独作为一部分
lst = s1.split()
print(lst)
lst = s2.split()
print(lst)
lst = s2.split(sep='|')
print(lst)
lst = s2.split(sep='|', maxsplit=1)
print(lst)
# 2、split()
# 从字符串右边部分开始劈分，默认的劈分字符是空字符串，返回的值都是一个列表
# 以参数sep指定劈分字符串的是劈分符
# 通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大劈分次数之后，剩余的子串会单独作为一部分
lst = s1.rsplit()
print(lst)
lst = s2.rsplit()
print(lst)
lst = s2.rsplit(sep='|')
print(lst)
lst = s2.rsplit(sep='|', maxsplit=1)
print(lst)

# 判断字符串的方法：
# 1、isidentifier()：判断字符串是不是合法表示符（字母、数字、下划线、汉字且数字不能作为开头）
# 2、isspace()：判断字符串是否全部由空白字符构成（回车、换行、水平制表符）
# 3、isalpha()：判断字符串是否全部由字母组成
# 4、isdecimal()：判断字符串是否全部由十进制数字组成
# 5、isnumeric()：判断字符串是否由数字构成（包括汉字数字、罗马数字等）
# 6、isalnum()：判断字符串是否全部由字母和数字组成
# 书写方法（以isidentifier()为例）
# 书写方法一：
s = '123qwe'
print(s.isidentifier())
# 书写方法二：
print('123qwe'.isidentifier())

# 字符串的替换：replace()
# 第一个参数指定被替换的子串，第二个参数指定替换子串的字符串
# 该方法返回替换后的字符串，替换前的字符串不发生变化
# 使用该方法时可用第三个参数替换指定最大替换次数
s1 = 'C++,C,Java'
print(s1.replace('Java', 'Python'))     # 用Python替换s1中的Java
s2 = 'C++,C,Java,Java,Java'
print(s2.replace('Java', 'Python', 2))     # 用Python替换s2中的Java，且最多只替换2次

# 字符串的合并：join()
# 将列表或元组中的字符串合并成一个字符串
lst = ['Hello', 'Java', 'Python']
print('|'.join(lst))  # 结果为Hello|Java|Python————>将列表lst中的各个元素用|串成字符串
print(''.join(lst))   # 结果为HelloJavaPython————>将列表lst中的各个元素直接串成字符串，什么都不添加

# 字符串的比较操作
# 运算符：>、<、>=、<=、==和!=
# 首先比较字符串中的第一个字符，若相等则比较下一个，直到出现不一样的字符为止，并停止比较
# 比较的是字符对应的ASCLL码

# 字符串的切片（具体方法同列表）
# 字符串是不可变类型，不能进行增、删、改操作
# 切片操作将产生新的对象
s1 = 'Hello,Baby'
s2 = s1[:5]+'!'+s1[6:]+'!'
print(s2)     # 结果为Hello!Baby!

# 字符串的格式化：用%和{}作为占位符
name = '张三'
age = 24
identity = '学生'
# 方式一：
'''
   字符串：%s
   整型：%d或%i
   浮点型：%f ————> %10.5f 表示该浮点型宽度为10，且精确到小数点后5位
'''
print('我的名字是%s。%d岁，是%s。' % (name, age, identity))
# 方式二：
'''
   {}中的数字是索引，若需要精确到某一位，则在索引后加冒号再进行操作
   {0：.3}  三位有效数字
   {0:10.3f}   宽度为10，精确到小数点后3位
'''
print('我的名字是{0}。{1}岁，是{2}。'.format(name, age, identity))
# 方式三：“f+字符串”模式
print(f'我的名字是{name}。{age}岁，是{identity}。')
