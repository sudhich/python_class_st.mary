import threading
import time

# Define a new class that extends the Thread class
class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    # Override the run method to define the behavior of the thread
    def run(self):
        print("Starting " + self.name)
        count = 0
        while count <= 5:
            time.sleep(self.delay)
            print(self.name + " count: " + str(count))
            count += 1
        print("Exiting " + self.name)

# Create two instances of the MyThread class
thread1 = MyThread("Thread-1", 1)
thread2 = MyThread("Thread-2", 2)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()
print("Main thread exiting...")
