# 作者： 世界第一大帅哥
# 开发时间 2022/2/22 12:44

def add_1(a, b):
    return a+b

print(add_1(10, 20))
# 直接这样写，其他模块在引用Module2时，除了add_1函数以外的内容也引用进来，即被引进模块中多了计算10+20的结果

if __name__ == '__main__':     # 需要加这样一行代码
    print(add_1(1000, 2000))   # 只有当点击运行Module2时，该语句才会被执行（被引进模块中没有出现1000+2000的结果）
