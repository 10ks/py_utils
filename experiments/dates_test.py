import time

t1 = time.time()
print("Seconds since epoch =", t1)

time.sleep(2)

t2 = time.time()
print("Seconds since epoch =", t2)

if t2 - t1 > 1:
    print("difference is > 1 sec")
else:
    print("difference is too small")

# local_time = time.ctime(seconds)
# print("Local time:", local_time)

#######################
# import threading
# import time


# def print_hello():
#     for i in range(4):
#         time.sleep(1)
#         print("Hello")


# def print_hi():
#     for i in range(4):
#         time.sleep(0.4)
#         print("Hi")


# t1 = threading.Thread(target=print_hello)
# t2 = threading.Thread(target=print_hi)
# t1.start()
# t2.start()
