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


obj1 = Employee(1,'何侃',27,'测试工程师',9000)
obj2 = Employee(2,'朱明华',30,'服务器工程师',18000)
obj3 = Employee(3,'凌云',28,'客户端工程师',14000)

obj1.displayEmployee()
obj2.displayEmployee()
obj3.displayEmployee()
print("公司总职工数: %d" % Employee.empCount,"人")

'''class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj1 = Foo('chengd',18)
print(obj1.name)
print(obj1.age)

obj2 = Foo('python',99)
print(obj2.name)
print(obj2.age)


class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)
 
   def displayEmployee(self):
      print ("Name : ", self.name,  "Salary: ", self.salary)
 
"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)'''
