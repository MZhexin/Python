# 作者： 世界第一大帅哥
# 开发时间 2022/1/13 13:37

# 面向过程与面向对象
# 任务：吃饭
# 面向过程：买菜、买油、先加什么、后加什么、怎么做菜
# 面向对象：打开手机点外卖，至于商家怎么做的菜就与我无关了（对于商家而言，就需要面向过程）

# 类与对象
# 类：多个类似事物组成群体的统称，即封装起来的数据及其操作（e.g. 列表、元组）——————>图纸（抽象）
# 对象：同一类下包含的相似的不同个例——————>根据图纸造出的车（实例）

# 创建类的方法：
'''
   class 类名:
      代码
'''
# 类的组成
'''
   1、类属性
   2、实例方法
   3、静态方法
   4、类方法
'''
class Student:  # Student是这个类的名称，类名由一个或多个英文单词组成，每个单词首字母大写，其余字母小写（大驼峰命名法）
    place = '北京'   # 类属性

    # 初始化方法
    def __init__(self, name, age):  # 基础格式为def __init__(self)，可以在self后面添加内容（init左右各两个下划线）
        self.name = name   # self.name称为实例属性，此处将局部变量name的值赋给实例属性self.name
        self.age = age     # 习惯上，实例属性和局部变量的名字相同

    # 实例方法
    # 在类外定义称为函数，在类中定义称为实例方法
    def method1(self):   # 括号内默认为self（不管写不写，最终都是self）
        print("这是实例方法")

    # 静态方法
    @staticmethod
    def method2():   # 静态方法此处不允许写self
        print('这是静态方法')

    # 类方法
    @classmethod
    def method3(cls):   # 括号内默认为cls（不管写不写，最终都是cls）
        print('这是类方法')


# 对象的创建（又称为类的实例化）
# 语法：实例名=类名（）
stu1 = Student('张三', 20)
# 执行实例方法method1()中的代码（下列两行代码的功能相同）
stu1.method1()            # 对象名.方法名()
Student.method1(stu1)     # 类名.方法名(对象名)
# 调用初始化方法中的name和age（具体数据为定义stu1时的'张三'和20）
print(stu1.name)
print(stu1.age)

'''
   1、类属性：在类中，方法外的变量称为类属性，被该类的所有对象所共享
   2、类方法：使用@classmethod修饰的方法，使用类名直接访问的方法
   3、静态方法：使用@staticmethod修饰的方法，使用类名直接访问的方法
'''



# 类属性的使用方式：
print(Student.place)     # 结果为：北京
# 不同对象名的类属性
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.place)     # 结果为：北京
print(stu2.place)     # 结果为：北京
# 修改之后的类属性
Student.place = '南京'
print(stu1.place)     # 结果为：南京
print(stu2.place)     # 结果为：南京



# 类方法的使用方式
Student.method3()



# 静态方法的使用方式
Student.method2()



# 动态绑定
# Python是动态语言，在创建对象之后，可以动态地绑定属性和方法
# 1、动态绑定属性
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
stu1.gender = '男'   # 创建stu1之后再动态绑定一个gender（只有stu1有，而stu2没有）
print(stu1.name, stu1.age, stu1.gender)
print(stu2.name, stu2.age)
# 2、动态绑定方法
def fun():
    print('这是动态绑定在stu1中的方法')
stu1.fun = fun()
stu1.fun



# 封装
# 在类Car中，所有的代码都被包在car下面，点击class Car:前面的减号可以隐藏代码，点击加号可以显示代码
class Car:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print("汽车已启动")
car=Car('宝马X5')
car.start()            # 写下car.之后系统会显示Car中所有可以使用的方法
print(car.brand)
#
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age   # 不希望age在类的外部被使用，故在self.和age之间加了两个下划线
    def show(self):
        print(self.name, self.__age)
stu = Student('张三', 20)
stu.show()          # 结果为：张三 20
print(stu.name)     # 结果为：张三
# print(stu.__age)  # 报错AttributeError，认为__age没有这个属性，不能被打印出来
print(stu._Student__age)  # 这样写就可以在类外使用age了（Student前面是.和一个下划线，后面是两个下划线）



# 继承
'''
   语法格式：
   class 子类类名(父类1, 父类2):
       pass
'''
# Python支持多继承
# 如果一个类没有继承任何类，则默认继承object
# 定义子类时，必须在其构造函数中调用父类的构造函数
'''
   class 子类(父类):
	def 子类的方法(self, 参数):
		super(子类，self).父类的方法(self, 参数)  # super中的self也必须写，但父类方法中不能写self
'''
# 代码实现：
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("姓名：{0} 年龄：{1}".format(self.name, self.age))
# 定义子类
class Student(Person):
    def __init__(self, name, age, number):
        super().__init__(name, age)    # 调用父类（即Person类）
        self.number = number
# 测试
stu = Student('Jack', 20, '1001')
stu.info()   # 子类中并没有定义info方法，此处的info方法是从父类中继承过来的



# 方法重写
# 如果子类对父类的某个属性或方法不满意，可以在子类中对其方法体进行重写
# e.g.子类想输出自己独有的东西，而父类不能满足这一需求，则需要方法重写
# 子类重写后的方法可以通过super().XXX()调用父类中被重写的方法
# 代码实现：
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("姓名：{0} 年龄：{1}".format(self.name, self.age))
class Student(Person):
    def __init__(self, name, age, number):
        super().__init__(name, age)    # 调用父类（即Person类）
        self.number = number
    def info(self):    # 左侧圆圈+箭头的图标表示重写方法
        super().info()  # 调用父类方法，表示先执行父类方法中的原代码，再执行下列重写后的代码
        print('学号：{0}'.format(self.number))
stu = Student('张三', 20, '001')
stu.info()



# object类
# object类是所有类的父类，因此所有类都有object类的属性和方法
# 内置函数dir()可以查看指定对象所有属性
class Student:
    pass
stu = Student()
print(dir(stu))    # 此行打印的所有结果，都是object类中所有的属性
print(stu)         # 此行打印的结果，是对象stu的内存地址
# object有一个__str__()方法，用于返回一个对于“对象的描述”
# __str__()方法对应于内置函数str()经常用于print()方法，帮我们查看对象的信息，所以我们经常会对__str__()重写
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):  # 重写__str__()，由于__str__()是默认父类object中的属性，所以可以直接重写
        return '我叫{0}，今年{1}岁了'.format(self.name, self.age)
stu = Student('张三', 20)
print(dir(stu))  # 此行打印的所有结果，依旧是object类中所有的属性
print(stu)   # 一旦重写__str__()，此行代码就不再输出对象的内存地址，而是根据重写的__str__()决定输出的内容



# 多态
# 多态————>具有多种形态
# 指即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法
# 在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法
# 只要对象有相应⽅法就能调⽤，与继承关系⽆关
class Animal(object):
    def eat(self):
        print('动物要吃东西')
class Dog(Animal):
    def eat(self):
        print('狗吃肉')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Person(object):
    def eat(self):
        print('人吃五谷杂粮')
def fun(animal):
    animal.eat()
fun(Dog())       # 结果为：狗吃肉
fun(Cat())       # 结果为：猫吃鱼
fun(Person())    # 结果为：人吃五谷杂粮
# Animal和Person继承了object
# Dog和Cat继承了Animal



# 静态语言与动态语言
# 静态语言与动态语言关于多态的区别
'''
   静态语言实现多态的三个必要条件：
   1、继承；
   2、方法重写；
   3、父类引用指向子类对象。
'''
'''
   动态语言的多态崇尚“鸭子类型”。
   只要看到一只鸟走起来像鸭子、游起来像鸭子、睡起来像鸭子，那么这只鸟就可以被称作“鸭子”。
   在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为
'''



# 特殊属性
'''
   1、# __dict__：获得对象所绑定的所有属性和⽅法的字典
   2、__class__：对象所属的类
   3、__base__：类对象的基类
   4、__bases__：类对象的⽗类
   5、__mro__：类的层次结构（所有父类、祖类等）
   6、__subclasses__：类对象的⼦类
'''



# 特殊⽅法
'''
   1、__new__：用于创建对象
   2、__init__：⽤于创建对象的初始化
   3、__str__：⽤来返回对象的地址，常将其重写⽤来返回对象的描述
'''



# 类的赋值、浅拷贝与深拷贝
class CPU:
    pass
class HardDisk:
    pass
class Computer:
    def __init__(self, CPU, HardDisk):
        self.CPU = CPU
        self.HardDisk = HardDisk
# 1、变量的赋值
# 只是形成两个变量，实际上还是指向同⼀对象
CPU1 = CPU()
CPU2 = CPU1
print(CPU1, id(CPU1))
print(CPU2, id(CPU2))    # 结果（内存地址）都一样，只是把一个对象放到两个变量中存储
# 2、浅拷贝
'''
   Python拷贝一般都是浅拷贝
   拷贝时，对象包含的子对象内容一般不拷贝，因此，源对象与拷贝对象会引用同一个子对象
   不拷⻉对象包含的子内容，源对象、拷⻉对象会指向同一⼦对象
'''
harddisk = HardDisk()   # 创建一个HardDisk类的对象
computer = Computer(CPU1, HardDisk)    # 创建一个Computer类的对象
import copy
computer2 = copy.copy(computer)
print(computer, computer.CPU, computer.HardDisk)
print(computer2, computer2.CPU, computer2.HardDisk)
# 3、深拷贝
# 使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
# 对象的子对象不拷贝
computer3 = copy.copy(computer)
print(computer, computer.CPU, computer.HardDisk)
print(computer3, computer3.CPU, computer3.HardDisk)
