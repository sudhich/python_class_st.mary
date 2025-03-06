
"""
sclass student:
    def __init__(self):
        print("automatically called when object is created.")
    def speaking(self,name,mobile_no):
        self.name=name
        self.mobile_no=mobile_no
        print(self.name,self.mobile_no)
    def listing(self):
        print(self.name,self.mobile_no)
s1=student()
s2=student() 
s1.speaking("sathwika","7800025689")
s2.speaking("charani","9347735279")
s1.listing()

        
#constructor
class mobile:
    def __init__(self,name,colour):
        print("hello how are you")
        self.name=name
        self.colour=colour
        print(name,colour)

redmi=mobile("REDMI","BLACK")
sams=mobile("samsung","white")

#constructor and method
#1
class student:
    def __init__(self,name,mobile):
        print("this is constructor")
        self.name=name
        self.mobile=mobile
        print(name,mobile)
    def speaking(self,msg):
        self.msg=msg
        print(msg)
        print("this is method")
        
msg="hello how are you"
s1=student("charani","9537210537")
s1.speaking(msg)

class car:
    def __init__(a,name,milage,color):
       a.name=name
       a.milage=milage
       a.color=color
    def speed(b):
        print(b.name,b.milage,b.color)
hc=car("hondacity","24.1","black")
hc.speed()
"""

#inheritance
"""
single
multiple
multilevel
hierarchical
hybird
"""
#single
"""

class A:
    def __init__(self):
        print("class A")
class B(A):
    def funn2(self):
        print("class B")

obj2=B()
obj2.funn2()
            

 """
'''
#multilevel
class A:
    def fun1(self):
        print("class A")
class B(A):
    def fun2(self):
        print("class B")
class C(B):
    def fun3(self):
        print("class C")

OBJ3=C()
OBJ3.fun3()
 

#multiple
class A:
    def fun1(self):
        print("class A")
class B:
    def fun2(self):
        print("class B")
class C:
    def fun3(self):
        print("class C")
class D(A,B,C):
    def fun4(self):
        print("class D")

obj1=D()
obj1.fun3()
obj2=B()
obj2.fun2()
'''
#hierarchical

class A:
    def fun1(self):
        print("class A")
class B(A):
    def fun2(self):
        print("class B")
class C(A):
    def fun3(self):
        print("class C")
class D(A):
    def fun4(self):
        print("")



        













        
        

    

