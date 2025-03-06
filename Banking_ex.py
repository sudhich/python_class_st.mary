import threading

balance = 0  # Shared resource
lock = threading.Lock()  # Create a lock

def deposit(amount):
    global balance
    lock.acquire()  # Acquire the lock
    try:
        balance += amount
    finally:
        lock.release()  # Release the lock

def withdraw(amount):
    global balance
    lock.acquire()  # Acquire the lock
    try:
        if balance >= amount:
            balance -= amount
        else:
            print("Insufficient balance")
    finally:
        lock.release()  # Release the lock

# Create threads
thread1 = threading.Thread(target=deposit, args=(1000,))
thread2 = threading.Thread(target=withdraw, args=(500,))
thread3 = threading.Thread(target=withdraw, args=(1500,))

# Start threads
thread1.start()
thread2.start()
thread3.start()

# Wait for threads to finish
thread1.join()
thread2.join()
thread3.join()

print(f"Final balance: {balance}")
