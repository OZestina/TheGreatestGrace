# 메인스레드: 파이썬 인터프리터가 제일 먼저 시작하는 부분
# 메인스레드는 여러 개의 서브 스레드를 만들어서 실행할 수 있다

# 쓰레드 관련 모듈은 thread, threading 이 있다 (하기에서는 threading 사용)
# .fork()
# .join()으로 만들어진 서브스레드의 종료를 기다렸다가 메인스레드를 종료하게 할 수 있다
#       => 서브스레드 종료 후 메인스레드에서 어떤 작업을 해야하는 경우

import threading
import time

class Worker(threading.Thread): # 스레드클래스 생성을 위해 threading.Thread 클래스 상속
    def __init__(self, name):
        super().__init__()        
        self.name = name      # thread 이름 지정

    def run(self):            # .start() 를 했을 때 실행되는 부분
        print("sub thread start", threading.currentThread().getName())
        time.sleep(2)
        print("sub thread end", threading.currentThread().getName())


print("main thread start")

threads = []
for i in range(5):
    thread = Worker(i)
    thread.start()
    threads.append(thread)

# .join() 을 하면 메인쓰레드가 서브스레드의 종료를 기다린 후 종료된다
for thread in threads:
    thread.join()

print("main thread end")
