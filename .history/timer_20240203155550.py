from threading import Timer
def hello():
    print('こんにちは')
time = Timer(10,hello)

time.start()