import time

start = time.time()
count = 0
while count < 10_000_000:
    count += 1
stop = time.time()
print(f"While loop took: {stop - start:.8f}s")



start = time.time()
for x in range(10_000_000):
    continue
stop = time.time()
print(f"For loop took: {stop - start:.8f}s")

