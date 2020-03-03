import threading
import time

def hello():
    print("hello, world")

t = threading.Timer(2.0, hello)
t.start()

while True:
    pass
