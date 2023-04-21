# 作者： 世界第一大帅哥
# 开发时间 2022/1/11 0:02

# else与for-in的搭配
print('else与for-in的搭配')
for item in range(3):
    password = input('请输入密码：')
    if password == '8888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('三次密码均错误')
    print('傻逼')
# 当密码输入正确后，执行break语句，跳出循环（包括与for循环并列的else）——>仅显示“密码正确”和“密码错误”（后者如果有的话）
# 当密码输入错误满三次后，继续执行程序（即与for并列的else）——>除了3次“密码错误”外，还显示“三次密码均错误”和“傻逼”


# else与while的搭配
print('else与while的搭配')
a = 0
while a < 3:
    password = input('请输入密码：')
    if password == '8888':
        print('密码正确')
        break
    else:
        print('密码错误')
        a += 1   # 在Python中最容易犯的错误之一就是while循环不改变变量
else:
    print('三次密码均错误')
    print('傻逼')
# 当密码输入正确后，执行break语句，跳出循环（包括与for循环并列的else）——>仅显示“密码正确”和“密码错误”（后者如果有的话）
# 当密码输入错误满三次后，继续执行程序（即与for并列的else）——>除了3次“密码错误”外，还显示“三次密码均错误”和“傻逼”
