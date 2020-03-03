import threading


def printit(a, b):
    # threading.Timer(2.0, lambda a: printit(3)  ).start()
    # threading.Timer(0.2, printit, [a, b]).start()
    
    t = threading.Timer(0.2, printit, [a, b])
    t.daemon = True
    t.start()
    print(a, b)


printit(2, 3)
input("Enter to stop")