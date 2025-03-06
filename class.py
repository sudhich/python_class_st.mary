#class

#Method

#1
"""
class Mobile:
    def funn(self,name,color):
        print("Hello how are you")
        print(name,color)
    
#redmi=Mobile()
redmi.funn("Redmi","Red")
print(id(Mobile))
print(id(redmi))

sams=Mobile()
redmi.funn("Redmi","Black")
sams.funn("Samsung","White")
"""
#2
"""
class Student:
    def __init__(self):
        print("Automatically called when object is created.")
    def speaking(self,name,mob_no):
        self.name=name
        self.mob_no=mob_no
        print(self.name,self.mob_no)
    def listing(self):
        print(self.name,self.mob_no)
s1=Student()
s2=Student()
s1.speaking("Monish","7800075689")
s2.speaking("Charani","7905673468")
s1.listing()
"""
"""
class A:
    def __init__(self):
        print("hi")
oj=A()
"""
"""
#Constructor
class Mobile:
    def __init__(self,name,color):
        print("Hello how are you")
        self.name=name
        self.color=color
        print(name,color)
    
  
redmi=Mobile("Redmi","Black")
sams=Mobile("Samsung","White")
"""
#contructor and method
""""
#1
class Student:
    def __init__(self,name,mob):
        print('This is constructor')
        self.name=name
        self.mob=mob
        print(name,mob)
    def speaking(self,msg):
        self.msg=msg
        print(msg)
        print("This is method")
    
msg="Hello how are you"
s1=Student("Charani","7800056345")
s1.speaking(msg)
"""
#2
"""
class Car:
    def __init__(a,name,milage,color):
        a.name=name
        a.milage=milage
        a.color=color
    def speed(b):
        print(b.name,b.milage,b.color)
    
hc=Car("HondaCity","24.1","Black")
hc.speed()

#Inheritance
'''
Single
Multiple
Multilevel
Hierarchical
Hybrid
"""
#Single
"""
class A:
    def __init__(self):
        print("Class A")
class B(A):
    def fun2(self):
        print("Class B")

obj2=B()
obj2.fun2()
"""
#Multilevel
#1
"""
class A:
    def fun1(self):
        print("Class A")
class B(A):
    def fun2(self):
        print("Class B")
class C(B):
    def fun3(self):
        print("Class C")


OBJ3=C()
OBJ3.fun3()
"""
#2
"""
class A:
    def __init__(self):
        print("Class A")
    def fun1(self):
        print("Class A")
class B(A):
    def fun2(self):
        print("Class B")
class C(B):
    def fun3(self):
        print("Class C")
    
OBJ1=C()
"""
#Multiple
"""
class A:
    def fun1(self):
        print("Class A")
class B:
    def fun2(self):
        print("Class B")
class C:
    def fun3(self):
        print("Class C")
class D(A,B,C):
    def fun4(self):
        print("Class D")
obj1=D()
obj1.fun3()
obj2=B()
obj2.fun2()
obj2.fun1()
"""
#Hierarchical
"""
class A:
    def fun1(self):
        print("Class A")
class B(A):
    def fun2(self):
        print("Class B")
class C(A):
    def fun3(self):
        print("Class C")
class D(A):
    def fun4(self):
        print("Class D")
    
obj1=D()
obj1.fun4()
"""
#Hybrid
"""
class A:
    def fun1(self):
        print("Class A")
class B(A):
    def fun2(self):
        print("Class B")
class C(A):
    def fun3(self):
        print("Class C")
class D(B,C):
    def fun4(self):
        print("Class D")
obj1=D()
obj1.fun4()
"""
#super method Program
#super() method to call base class constructor example
#1st method is If we to access a method any other class to any other class
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
st1 = Student("shiva", 17)
st1.test()
"""
#2
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name,self.age)
#If you want to access any atribute of any other to other class so we use self.attribute_name


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
st1 = Student("shiva", 17)
"""
#3
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name,self.age)
    def work(self):
        print("person is working in TCS Company")
    def standing(self):
        print("If you are not able to tell the answer you have to standup")

class Student(Person):
    def __init__(self, name, age):
        #Person.__init__(self,name,age)
        #Person.work(self)
        #super().__init__(name,age)
        #super().work()
        super().standing()
        Person.standing(self)
    
st1 = Student("shiva", 17)

#a=10
#print(id(a))
print(id(Student))
print(id(st1))

"""
#Overloading
"""
class Calculator:
    def add(self, a, b=0, c=0):  # Overloading using default arguments
        return a + b + c

# Creating an object
calc = Calculator()

# Calling the overloaded method
print(calc.add(10))          # Output: 10
print(calc.add(10, 20))      # Output: 30
print(calc.add(10, 20, 30))  # Output: 60
"""
"""
#Overriding
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):  # Overriding the speak method
        return "Dog barks"

class Cat(Animal):
    def speak(self):  # Overriding the speak method
        return "Cat meows"

# Creating objects
animal = Animal()
dog = Dog() 
cat = Cat()

# Calling the overridden methods
print(animal.speak())  # Output: Animal speaks
print(dog.speak())     # Output: Dog barks
print(cat.speak())     # Output: Cat meows

#Create ENV and activate and install flask
"""
"""
Microsoft Windows [Version 10.0.19045.5371]
(c) Microsoft Corporation. All rights reserved.

C:\Users\sudhir>python -m venv myenv

C:\Users\sudhir>python -m venv charani

C:\Users\sudhir>myenv\Scripts\activate

(myenv) C:\Users\sudhir>charani\Scripts\activate
(charani) C:\Users\sudhir>charani\Scripts\activate
(charani) C:\Users\sudhir>python --version
Python 3.13.0

(charani) C:\Users\sudhir>flask --version
'flask' is not recognized as an internal or external command,
operable program or batch file.

(charani) C:\Users\sudhir>pip flask
ERROR: unknown command "flask"

(charani) C:\Users\sudhir>pip install flask
Collecting flask
  Downloading flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting Werkzeug>=3.1 (from flask)
  Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from flask)
  Downloading jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2 (from flask)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from flask)
  Downloading click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting blinker>=1.9 (from flask)
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting colorama (from click>=8.1.3->flask)
  Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->flask)
  Downloading MarkupSafe-3.0.2-cp313-cp313-win_amd64.whl.metadata (4.1 kB)
Downloading flask-3.1.0-py3-none-any.whl (102 kB)
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading click-8.1.8-py3-none-any.whl (98 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.5-py3-none-any.whl (134 kB)
Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
Downloading MarkupSafe-3.0.2-cp313-cp313-win_amd64.whl (15 kB)
Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Installing collected packages: MarkupSafe, itsdangerous, colorama, blinker, Werkzeug, Jinja2, click, flask
Successfully installed Jinja2-3.1.5 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 colorama-0.4.6 flask-3.1.0 itsdangerous-2.2.0

[notice] A new release of pip is available: 24.2 -> 25.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip

(charani) C:\Users\sudhir>flask --version
Python 3.13.0
Flask 3.1.0
Werkzeug 3.1.3

(charani) C:\Users\sudhir>"""
# Third party Package
#1 Math Package
"""Sqrt()
cos()
sin()
pow()
degree()
fabs()"""
#2 Date Time Package



