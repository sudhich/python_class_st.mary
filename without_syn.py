import threading

# Without synchronization
counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"Counter value: {counter}\n")

# Create threads without synchronization
threads = []
for i in range(10):
    t = threading.Thread(target=increment_counter)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Without synchronization, final counter value:", counter)

