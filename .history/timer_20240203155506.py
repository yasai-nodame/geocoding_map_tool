from threading import Timer
def hello():
    for i in range(10):
        print('こんにちは')
time = Timer(1,hello())

time.start()