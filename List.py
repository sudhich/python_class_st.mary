
lst=["Naresh", 20, 62.5, 56]
'''
print(lst)


#Access
print(lst[2])
print(lst[-1])
#Slicing
#[start:end:step]
print(lst[0:5:3])
print(lst[::-1])

#Update
print(lst)
lst[1]=19
print(lst)

#add
print(lst)
lst.append('M')
print(lst)
'''
"""
lst=[]
for i in range(11):
    lst.append(i)
print(lst)

"""
"""
#Deletion remove()
print(lst)
lst.remove(20)
print(lst)


#slice
print(lst)
print(lst[::-2])
"""
"""
#Looping of list
for i in [1,2,3,45]:
    print(i)

#Join list
l1=[1,2,3]+[4,5,6]
print(l1)

#Repation of llist
l2=[2,3,4,5]*3
print(l2)


#Membership(in, not in)
print(2 not in [1,2,3])
"""
"""
#MAX,MIN,SORTED,SUM
print(max([4,1,78,4,-1]))
print(min([4,1,78,4,-1]))
print(sorted([4,1,78,4,-1]))
print(sum([4,1,78,4,-1]))
"""

#Nested
"""
l=[1,2,3,[4,5,6,[7,8],9],10]
print(l[3][3][1])
"""
"""
#for i in l:
#    print(it)
print(l[3][0])
print(l[-2][-5])
"""
#set
"""#print(list(set([1,"hello",24.5])))
lst=set()
print(type(lst))
lst.add(3)
print(lst)
lst.update([1,3,4])
print(lst)
lst.remove(5)
lst.discard(6)
lst.pop()
print(lst)"""
#dict
"""
Sat_det={"name":"Sathivika","age":16,"weight":40.500}
print(Sat_det)
print(Sat_det.keys())
print(Sat_det.values())
print(Sat_det["age"])
Sat_det["age"]=15
print(Sat_det)
Sat_det["percentage"]=70
print(Sat_det)
del Sat_det["age"]
print(Sat_det)
"""
Sat_det={"name":"Sathivika","age":16,"weight":40.500}
"""
for i in Sat_det.keys():
    print(i)

for i in Sat_det.values():
    print(i)
"""
"""
for i in Sat_det.items():
    print(i)

for key, value in Sat_det.items():
    print(key, value)
"""
"""
print({i:i*i for i in range(6)})
"""
#Input Function
a=float(input("Enter the number"))
print(type(a))
print(a)
