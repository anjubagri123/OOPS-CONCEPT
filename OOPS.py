# # # # # Object is a single entity having attributes, and functions,and occupied space in the memory
# # # # #class is an Blueprint for creating an object,not occupied space
# # # # #constructor is an special function which is called when an object is initaited
# # # # class Student:
# # # #     name = "Aadi"
# # # #
# # # #     def __init__(self):
# # # #         print("how are you?\U0000FE0F \u2764\uFE0F",end = " ")
# # # #
# # # # Obj = Student()        #object created - object also known as instance
# # # #
# # # # print(Obj.name,"\U0001f600")
# # # # #############################
# # # # class Student:
# # # #     college_name = "GJU"         #this is stored for only one time in memory but name is every time because for every object
# # # #     #All class have this __init__ function this is called constructor an special function and it is invoked automatically as created the object
# # # #     # There are two type of constructor--> 1. Default and other one is parameterised constructor
# # # #     def __init__(self):
# # # #         print("Hello i am default constructor")        #if i don't have print statement then i won't be print anything this is by default made by python
# # # #
# # # #     def __init__(self,name,marks):           #instead of self i can also write anything here,this is parameterised constructor
# # # #         self.name = name           #these both lines are optional we can directly use the name,marks like in third line
# # # #         self.marks = marks
# # # #         print("New Student Added and his marks is:",name,marks)
# # # # name = ""
# # # # while(name != "0"):
# # # #     name = input("ENter the name: ")
# # # #     marks = input("Enter ur marks: ")
# # # #     obj = Student(name,marks)
# # # # print(obj.college_name)
# # # # print(Student.college_name)     #both are valid
# # # # # obj2= Student()       this will not work
# # # #
# # # # # there are two type of attributes-1.Instance attributes , 2. Class Attribute
# # # # # Instance Attribute having different values for each object ,but class Attribute is having same value for each object
# # # # # eg. name is instance attribute and branch,state,class will be class attribute of object
# # # # # Instance attribute need to use self.name,self.class etc...
# # # # # If i define name attr as an class attr and also as an Instance attribute then object attribute always print because precedence of it is always high
# # # # # object attr > class attr generally we dont do like that but we can just for the sake of giving the by default value where the user forgot give the value of name
# # # # # class has two things- 1. Data/Attributes , 2. Functions/Methods
# # # # # eg. Car's color,milege,engine cc,etc means its property | Methods are How Car Starts,How car run,how car stop etc.. '
# # # # # Functions that are written in class called methods
# # # # # String,list,Dictionary are the Classes and we have the methods for it
# # # #
# # # class Car:
# # #     def __init__(self):
# # #         self.name = "Aditya"
# # #
# # #     def hello(self):
# # #         print("Best Wishes Welcome to our Showroom")
# # #         # return "Good night"
# # #     def Wish(self,car_type):
# # #         self.car_type = car_type
# # #         print("we will buy this",car_type,self.name)      #will print maruti
# # # obj = Car()
# # # # ans = obj.hello()       # for storing returned values
# # # obj.hello()
# # # # print(obj.Wish("maruti"))
# # # # print(ans)
# # # # obj.Wish("marcedeese")
# # # # obj.Wish("marcedees")
# #
# # #####################################
# # # class student:
# # #     # Total_mark = 0
# # #
# # #     def __init__(self,name,marks):
# # #         # self.name = "Aadi"
# # #         # self.marks = [20,34,46]
# # #         print("name and marks of",name,marks)
# # #         print("Hello")
# # #     def avg_func(self,Total_marks):
# # #         # for i in self.marks:
# # #         #     Total_marks += self.marks[i]
# # #         print("Total marks will be:",Total_marks)
# # #         self.avg = Total_marks/3
# # #         return self.avg
# # # name = "Aadi"
# # # # marks = [24, 34, 46]
# # # marks = []
# # # while(1):
# # #     mark = int(input("Enter marks:"))
# # #     marks.append(mark)
# # # print("My list is:",marks)
# # #
# # #
# # # obj = student(name,marks)
# # # total_marks=0
# # # for i in range(len(marks)):
# # #     total_marks +=  marks[i]
# # # ans = obj.avg_func(total_marks)
# # # print(ans)
# #
# # ####################################
# # # class student:
# # #
# # #     def __init__(self,name,marks):
# # #         self.name=name
# # #         self.marks=marks
# # #     def func_avg(self):
# # #         sum=0
# # #         for i in range(len(self.marks)):
# # #             sum+=self.marks[i]
# # #         print(sum,len(self.marks))
# # #         avg=sum/len(self.marks)
# # #         print("Average of",self.name,"'s marks will be:",avg)
# # #
# # # obj = student("Aditya",[90,89,80])
# # # obj.func_avg()
# # # obj.name = "Aadi"
# # # obj.func_avg()
# # #methods that dont having self in their parameter (work at class level)
# # ###################
# # # class student:
# # #
# # #     def __init__(self, name, marks):
# # #         self.name = name
# # #         self.marks = marks
# # #
# # #     # def hello():            #if i dont write self as parameter in this function then error will be given so we need to make this function as static
# # #     #     print("Hello")
# # #     #as in this way - use decorator called @staticmethod above the declaration of function
# # #     @staticmethod
# # #     def Wishes():
# # #         print("Always be happy")
# # #
# # #     def func_avg(self):
# # #         sum = 0
# # #         for i in range(len(self.marks)):
# # #             sum += self.marks[i]
# # #         print(sum, len(self.marks))
# # #         avg = sum / len(self.marks)
# # #         print("Average of", self.name, "'s marks will be:", avg)
# # #
# # #
# # # obj = student("Aditya", [90, 89, 80])
# # # obj.func_avg()
# # # obj.name = "Aadi"
# # # obj.func_avg()
# # # obj.Wishes()
# # #########################
# # # Abstraction: Hiding the essential details of class and showing only the essential one to the user.
# # # Encapsulation: Wrapping data and functions into a single unit(object).
# #
# # # class car:
# # #     def __init__(self):
# # #         self.acc = False
# # #         self.clutch = False
# # #         self.brk = False
# # #     def Start(self):
# # #         self.clutch = True
# # #         self.acc= True
# # #         self.brk = True
# # #
# # #         print("car started....")
# # #
# # # obj = car()
# # # obj.Start()
# # #################################
# # # class Account:
# # #     def __init__(self,balance,account_no):
# # #         self.balance = balance
# # #         self.account_no = account_no
# # #     def debit(self,amt):
# # #          self.balance -= amt
# # #          print("Rs.",amt," is debited")
# # #          print("Total Balance =",self.get_balance())
#
# # #     def credit(self,amt):
# # #          self.balance +=amt
# # #          print("Rs.", amt, " is credited")
# # #          print("Total Balance =",self.get_balance())
# # #     def get_balance(self):
# # #         # print("Your balance is:",self.balance)
# # #         return self.balance
# # #
# # # obj = Account(10000,123)
# # # print(obj.balance)
# # # print(obj.account_no)
# # # obj.debit(200)
# # # obj.credit(1000)
# # # obj.get_balance()
# # ##################################333
# # # some we create object but they are not going to be used in future then the best practice is to delete that object beacuse it unnecessrily taking the memory
# # # so for that
# #
# # class Sample:
# #     def __init__(self,name):
# #         self.name = name
# #         print("welcome to Sample Class")
# #     def add(self,a,b):
# #         ans = a+b
# #         return ans
# # obj = Sample("Anju")              #to call constructor
# # print("addition will be:",obj.add(23,56))
# #
# # #now delete this object and its properties
# # # del obj    or
# # print("Before Delete object:",obj)
# # print("Before Delete name:",obj.name)
# # del obj.name
# # print("before Delete object:",obj)
# # print("After delete name:",obj.name)
# # # print("Object deleted successfully..")
# # #now if i try to access this object or its want to access its property then we cant do it
# # # error will be like this:Traceback (most recent call last):
# # #   File "C:\Users\bagri\OneDrive\Desktop\DSA\OOPS.py", line 199, in <module>
# # #     obj.add(2,5)
# # #     ^^^
# # # NameError: name 'obj' is not defined
# #
# # # obj.add(2,5)         So this should be in comment for not giving error
# ###########################################
# # class Account:
# #     def __init__(self,account_no,pwd):
# #         self.account_no = account_no
# #         self.pwd = pwd
# # obj = Account("Anju",2345244)
# # print(obj.account_no)
# # print(obj.pwd)             #its security breaching
# # To prevent from it we need to make the variables to private for security purpose
# class Account:
#     def __init__(self,account_holder,pwd):
#         self.account_holder = account_holder
#         self.__pwd = pwd        #to make this private use two underscore before the variable name
#     def Change_pass(self):
#         print(self.__pwd)
#     def __CheckBalance(self,chkblce):
#         self.chkblce = chkblce
#         print("hello your balance is Msg from Admin",self.chkblce,"/- Rs.")
#     def Admin(self):
#         print(self.__CheckBalance(100))
# obj = Account("Anju",2345244)
# # print(obj.account_holder)
# # print(obj.__pwd)       cant access   because this satement is outside of class
# # we can print pwd but inside the class
# # obj.Change_pass()
# #private attribute & methods are meant to be used within the class and are not from outside the class
# # obj.__CheckBalance("100")       #we cant see it because this method is private --> so why we make this private function we make this because internally a function we can use it
# obj.Admin()
# ##############################
# # There are four pillers of OOPS - 1.Abstraction,2. Encapsulation, 3.Inheritance 4. Polymorphism
# # Inheritance - when a class derives the properties of & methods of another class(parent/base).
#
# class Animal:
#     color="black"
#     @staticmethod          #making static beca use we have not given self parameter in the function
#     def can_breath():
#         print("Yes Its breathing")
#
#     @staticmethod
#     def can_talk():
#         print("Yes its talking")
#
#
# class dog(Animal):
#     def __init__(self,type):
#         self.type = type
#
# obj1 =dog("dogie")
# obj2 =dog("catty")
# print(obj1.type)
# print(obj2.can_talk())       # here we have used the parent class method with the help of child class object
# print(obj1.can_breath())
#
# print(obj1.color)
# #inheritance are of multiple types - 1. Single Inheritance , 2. Multiple Inheritance, 3. Multilevel Inheritance , 4. hybrid, 5. Heirarchial
# # Above example is the single Inheritance
#this is Mutilevel inheritance
# class dadu:
#     @staticmethod
#     def foji():
#         print("I am foji..\U0000FE0F \u2764\uFE0F")
# class papa(dadu):
#     @staticmethod
#     def lib():
#         print("I am Librarian..\U0000FE0F \u2764\uFE0F")
# class me(papa):
#     @staticmethod
#     def engg():
#         print("I am Engineer...\U0000FE0F \u2764\uFE0F")
# obj1 = me()
# print(obj1.engg())
# print(obj1.foji(),obj1.lib())     #i can also run parent class and the grandparent class

####################################
#multiple Inheritance
# class papa:
#     @staticmethod
#     def sasur():
#         print("I am your father in law")
# class bhaibda(papa):
#     @staticmethod
#     def jeth():
#         print("I am ur jeth ji")
# class chotabhai(papa):
#     @staticmethod
#     def devar():
#         print("I am your brother in law")
# obj1 = chotabhai()            #chotabhai k obj se chotabhai m jo function aur yeh papa ko derive kiya h to uska function yeh do call krskte h
# obj2 = bhaibda()       #same bhaibda can call its own function and its deriving class function
# obj1.devar()
# obj1.sasur()
# obj2.jeth()
# obj2.devar() cant
###########################
# super() method is used to access methods of the parent class
# when there is two function in differnt class with the same name then if i want to call the function of parent class only then used super()
###########
# class papa:
#     def __init__(self,type):
#         self.type=type
#         print(type)
#         print("Hello i am from papa class")
#     @staticmethod
#     def sasur():
#         print("I am your father in law")
#
# class chotabhai(papa):
#     def __init__(self,name,type):
#         print("Hello i am from chotabhai class")
#         super().__init__(type)
#
#         self.name = name
#
#     @staticmethod
#     def devar():
#         print("I am your brother in law")
# obj1 = chotabhai("rishte","Anek")            #chotabhai k obj se chotabhai m jo function aur yeh papa ko derive kiya h to uska function yeh do call krskte h
# obj2 = bhaibda()       #same bhaibda can call its own function and its deriving class function
# obj1.devar()
# obj1.sasur()
# obj2.jeth()

# obj1.__init__()
# obj1.__init__()        #bcoz of the same name it is running for the derived class only means its own class
#for i want to run for parent then use super()

##################################
# class method- it is bound to the class and receives the class as an implicit first argument
# Note- static method cant access  or modify class state & generally for utility
###########################33
# class person:
#     name = "anonymous"
#     def Change_name(self,name):
#         self.name = name
#
#
# obj = person()
# obj.Change_name("Rahul")
# print(obj.name)
# print(person.name)
######################
# class person:
#     name = "anonymous"
#
#     def Change_name(self, name):
#         self.name = name
#
#
# obj = person()
# obj.Change_name("Rahul")
# print(obj.name)
# print(person.name)
#############################
# class person:
#     name = "anonymous"
    # def Change_name(self, name):
        # self.name = name
       #one method to change  class 's name variable is
       # person.name = name   # from that both will be the Rahul
        # or
       # print("third",self.__class__.name)
        # or by commenting this function and make a new class method
#     @classmethod
#     def Change_name(cls,name):
#         cls.name=name
#         print("itself:",cls.name)
#
# obj = person()
# obj.Change_name("Rahul")
# print("First",obj.name)
# print("Second",person.name)

#########################################
# There are three decorator :-
# 1. @staticmethod, 2. @classmethod, 3. @property, 4. @getter, 5. @setter
# Methods are different types:-
# 1. static method- Nothting in parameter.They dont use the class and instance methods 's functions and attributes
# 2. Instance Method- They have self as an first argument
# 3. Class Mathod- They have cls as an first argument
#############################################
# class Student:
#     def __init__(self,eng,hin,math):
#         self.eng = eng
#         self.hin = hin
#         self.math = math
#         self.percentage = str((self.eng+self.hin+self.math)/3)+"%"
# obj = Student(99,89,80)
# print("percentage will be:",obj.percentage)
#
# obj.eng=90
# print(obj.eng)
# print(obj.percentage)      #percentage is again same but this is not correct bcoz eng marks has decreased for that we need to make a function called percentage
############################################################
############################################
# class Student:
#     def __init__(self,eng,hin,math):
#         self.eng = eng
#         self.hin = hin
#         self.math = math
#
#     def Calculate_percentage(self):
#         self.percentage = str((self.eng + self.hin + self.math) / 3) + "%"
#         return self.percentage
#
# obj = Student(99,89,80)
#
#
# obj.eng=90
# print(obj.eng)
#
#
# print("Calling Function :",obj.Calculate_percentage())
#########this thing can be more easy using property decorator
# class Student:
#     def __init__(self,eng,hin,math):
#         self.eng = eng
#         self.hin = hin
#         self.math = math

    # def Calculate_percentage(self):
    #     self.percentage = str((self.eng + self.hin + self.math) / 3) + "%"
    #     return self.percentage
    #by replacing this function use
#     @property
#     def percentage(self):
#         return  str((self.eng + self.hin + self.math) / 3) + "%"
#
# obj = Student(99,89,80)
# print("From before property:",obj.percentage)
#
# obj.eng=90
# print("From after property:",obj.percentage)

# print(obj.eng)
# print("From property: ",obj.percentage())   dont need to call this as we change in marks our percentage will change automatically

# print("Calling Function :",obj.Calculate_percentage())
# property- we use @property decorator on any method in the class to use the method as a propperty
#################################################
# Polymorphism : poly means many and morphism means forms - when the same operator is allowed to have different meaning according to the context

# name = "Anju " + "Bagri"       #concatenate
# sum = 12+23                   #add
# li = [2,4,6]+[1,2,3]  #merge
# print(name)
# print(sum)
# print(li)
#int,string,list all are class in the python and these i have given is the object for the class
#######################################
class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def ShowNumber(self):
        number = str(self.real) + "i + " +str(self.img) + "j"
        return number

    def __add__(self,obj1):
        # ans = str(obj.real+obj1.real) +"i +" + str(obj.img+obj1.img) + "j"
        newReal = str(obj.real+obj1.real)
        newImg =  str(obj.img+obj1.img)
        return complex(newReal,newImg)

    def __sub__(self, obj1):
        # ans = str(obj.real+obj1.real) +"i +" + str(obj.img+obj1.img) + "j"
        newReal = str(obj.real - obj1.real)
        newImg = str(obj.img - obj1.img)
        return complex(newReal, newImg)

    def __mul__(self, obj1):
        # ans = str(obj.real+obj1.real) +"i +" + str(obj.img+obj1.img) + "j"
        newReal = str(obj.real * obj1.real)
        newImg = str(obj.img * obj1.img)
        return complex(newReal, newImg)
obj = complex(12,34)
obj1 = complex(34,3)

print("first Number:",obj.ShowNumber())
print("Second Function:",obj1.ShowNumber())

# ans = obj.add_comp(obj1)
# print(ans.ShowNumber())
# ans = complex.add_comp(obj,obj1)
# print("Complex numbers addition will be: ",complex.add_comp(obj,obj1))
#dunder function means double underscore

ans_add = obj + obj1
print("output from Add dunder function: ",ans_add.ShowNumber())

ans_sub = obj - obj1
print("output from Sub dunder function: ",ans_sub.ShowNumber())

ans_mul = obj * obj1
print("output from Mul dunder function: ",ans_mul.ShowNumber())
# i want that when write ans = obj + obj1 will get added
# but it will give me error so i should make my add function as dunder function as add--> __add__()

#####################################################3
import math
class circle:
    def __init__(self,radi):
        self.radi = radi
    def Area(self):
        return math.pi * pow(self.radi,2)
    def Perimeter(self):
        return 2* math.pi*self.radi

c1 = circle(21)
print("Area of circle: ",c1.Area())
print("Perimeter of circle: ",c1.Perimeter())
##############################
class Employee:
    def __init__(self,role,sal,dept):
        self.role = role
        self.sal =sal
        self.dept =dept
    def ShowDetails(self):
        return self.role,self.sal,self.dept
e1 = Employee("Tester",23000,"Imaging")
print(e1.ShowDetails())
#############################
class Employee:
    def __init__(self,role,sal,dept):
        self.role = role
        self.sal =sal
        self.dept =dept
    def ShowDetails(self):
        # return self.role,self.sal,self.dept
        print("Role = ",self.role)
        print("Salary =  ",self.sal)
        print("Dept = ",self.dept)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","230000","R&D")
    def ShowInfo(self,name,age):
        print("Name = ",self.name)
        print("Age = ",self.age)

# e1 = Employee("Tester",23000,"Imaging")
# e1.ShowDetails()

engg1 = Engineer("Elon Musk","50")
engg1.ShowDetails()
engg1.ShowInfo("Anju","23")
##################################3
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,ord2):
        return self.price > or2.price





or1 = Order("chips",20)
or2 = Order("Burger",50)

print(or1 > or2)

#######################################3