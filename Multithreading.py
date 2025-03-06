import time
import threading

def calc_square(numbers):
    print("Calculate square numbers")
    for n in numbers:
        time.sleep(1)
        print('square:', n * n)

def calc_cube(numbers):
    print("Calculate cube of numbers")
    for n in numbers:
        time.sleep(1)
        print('cube:', n * n * n)

arr = [2, 3, 4, 5, 6, 7, 8, 9]
t = time.time()
print(t)

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))
print(t1.is_alive())
t1.start()
t2.start()
print("\n",t1.is_alive(),"\n")
print(t1.name)
t1.join()
t2.join()

print("Done in :", time.time() - t)
