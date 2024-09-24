import time

start = time.time()
for i in range(100000000):
    j = i * i
end = time.time()
print("The time of execution of above program is :", (end - start), "s")
print('==================================')
