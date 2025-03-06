def check_age(age):
    if (age<18):
        raise ValueError("Age should be at least 18 years to Vote")
    else:
        print("You are eligible for Voating")
age=int(input("Enter the age: "))
try:
    check_age(14)
except ValueError as e:
    print(e)
