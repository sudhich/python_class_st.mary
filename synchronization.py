import threading

# Reset counter for the next example
counter = 0

# With synchronization using Lock object
lock = threading.Lock()  # Create a lock

def increment_counter_sync():
    global counter
    lock.acquire()  # Acquire the lock
    try:
        counter += 1
        print(f"Counter value: {counter}")
    finally:
        lock.release()  # Release the lock

# Create threads with synchronization
threads_sync = []
for i in range(10):
    t = threading.Thread(target=increment_counter_sync)
    threads_sync.append(t)
    t.start()

for t in threads_sync:
    t.join()

print("With synchronization, final counter value:", counter)

