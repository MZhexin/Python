# 作者： 世界第一大帅哥
# 开发时间 2022/1/4 16:31

# 用print进行输出(数字、字符串、表达式）
# 数字
print(20)
# 字符串
print("I am so handsome")
# 表达式
print(3+1)

# 将数据输入到文件中
# 注意点： 1、所储存的盘符需要存在； 2、需要使用file=fp
fp=open('C:\\Users\\31505\\Desktoptext.txt','a+')  #a+用法：如果文件不存在就创建一个文件，如果文件已经存在，就在文件后面追加内容
print("Hello world!",file=fp)
fp.close()
# 不进行换行输出
print("Hello", "World", "!")

