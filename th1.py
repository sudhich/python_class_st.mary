import threading

def add():
    a=10
    b=20
    c=a+b
    print(c)
def sub():
    a=20
    b=3
    c=a-b
    print(c)

t1=threading.Thread(target=add)
t2=threading.Thread(target=sub)
t1.start()
print(t1.name)
t1.join()
t2.start()
print(t2.name)
t2.join()
