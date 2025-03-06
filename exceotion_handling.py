"""y=0
x=5
print(x/y)
try:
    print(x/y)
except:
    print("This is ZeroDivisionError")
finally:
    print("It is always executed")
"""
"""
try:
    a=1
    if(a==1):
        prin("Hello")
except Exception as e:
    print(e)

finally:
    print("It is always executed")

"""
"""
a=1
if(a==1):
    prin("hello")
"""

try:
    num1=int(input("Enter the 1st No"))
    num2=int(input("Enter the 2nd No"))
    result=num1/num2
except ValueError:
    print("Please enter the valid integer")
except ZeroDivisionError:
    print("Can not divide by zero")
else:
    print("The result of division is:",result)
finally:
    print("This block is always executed")
"""
"""
"""
try:
    num1=int(input("Enter the 1st No"))
    num2=int(input("Enter the 2nd No"))
    result=num1/num2
except ValueError:
    print("Please enter the valid integer")
except ZeroDivisionError:
    print("Can not divide by zero")
else:
    print("The result of division is:",result)
finally:
    print("This block is always executed")
"""
#4ways we can write except block.
#1-->except:
#2-->except Exception_Class ex-   except ZeroDivisionError:
#3-->except (Exception_Class1,Exception_Class2,----)
#4-->except Exception_Class1 as obj: ex--except Exception as e:
"""
a,b,c=3,4,5
avg=(a+b+c)/3
print("excepted out is",avg)
a,b,c=3,4,5
avg=(a+b*c)/3#This is logical error
print("Acual out is",avg)
"""
