from threading import Timer
def hello():
    print('こんにちは')
time = Timer(1,100)

time.start()