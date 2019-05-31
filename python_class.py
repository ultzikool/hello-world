print("类的基础练习")
class Employee:
    '所有员工的基类'
    empCount = 0

    
    def __init__(self, num, name, age, job, salary):
        self.num = num
        self.name = name
        self.age = age
        self.job = job
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print (self.num,'、'"职工名称:", self.name, ", 年龄:", self.age,"岁", ", 职位:", self.job, ", 工资:",self.salary,"元/月")


obj1 = Employee(1,'Peter',27,'测试工程师',10000)
obj2 = Employee(2,'John',30,'服务器工程师',18000)
obj3 = Employee(3,'steve',28,'客户端工程师',16000)

obj1.displayEmployee()
obj2.displayEmployee()
obj3.displayEmployee()
print("公司总职工数: %d" % Employee.empCount,"人")

print()
print()
print()



print("类的练习1")

print("""题目：游戏人生程序

1、创建三个游戏人物，分别是：

苍井井，女，18，初始战斗力1000
东尼木木，男，20，初始战斗力1800
波多多，女，19，初始战斗力2500

2、游戏场景，分别：

草丛战斗，消耗200战斗力
自我修炼，增长100战斗力
多人游戏，消耗500战斗力""")

print()
print()
print()

class Character:

    def __init__(self, name, gender, age, fig):
        self.name = name
        self.gender = gender
        self.age = age
        self.fight = fig

    def grassland(self):        #注释：草丛战斗，消耗200战斗力
        self.fight = self.fight - 200

    def practice(self):         #注释：自我修炼，增加100战斗力
        self.fight = self.fight + 100

    def incest(self):           #注释：多人游戏，消耗500战斗力
        self.fight = self.fight - 500
    
    def detail(self):           #注释：当前对象的详细情况
        temp = "姓名:%s ; 性别:%s ; 年龄:%s ; 战斗力:%s" % (self.name, self.gender, self.age, self.fight)
        print (temp)
        

###################开始游戏#########################


cang = Character('苍井井','女','18',1000)   
dong = Character('东尼木木','男','20',1800)  
bo = Character('波多多','女','19',2500)

cang.detail()
dong.detail()
bo.detail()

print()

print("进行一次战斗")
cang.grassland()
dong.practice()
bo.incest()

print()

print("输出当前所有人的详情:")
cang.detail()
dong.detail()
bo.detail()

print()

print("再进行一次战斗")
cang.practice()
dong.incest()
bo.grassland()

print()

print("输出当前所有人的详情:")
cang.detail()
dong.detail()
bo.detail()

print()
print()
print()

print("类的练习2")

print("""猫可以：喵喵叫、吃、喝、拉、撒

狗可以：汪汪叫、吃、喝、拉、撒""")

class Animal():

    def eat(self):
        print("%s 会吃" %self.name)

    def drink(self):
        print("%s 会喝" %self.name)

    def shit(self):
        print("%s 会拉" %self.name)

    def pee(self):
        print("%s 会撒" %self.name)

class Cat(Animal):

    def __init__(self, name):
        self.name = name
        self.breed = "猫"

    def mmj(self):
        print("%s 会喵喵叫" %self.name)

class Dog(Animal):

    def __init__(self, name):
        self.name = name
        self.breed = "狗"

    def wwj(self):
        print("%s 会汪汪叫" %self.name)

########执行##############
    
c1 = Cat("小梅家的猫")
c1.eat()

c2 = Dog("兜兜家的狗")
c2.wwj()
