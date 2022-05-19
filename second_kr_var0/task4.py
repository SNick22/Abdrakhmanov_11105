from threading import Thread
from time import sleep
from random import randint

common_list = []


# def func(n):
#     sleep(randint(0, 5))
#     common_list.append(n)
#
#
# threads = []
# for i in range(20):
#     th = Thread(target=func, args=(i,))
#     threads.append(th)
#     th.start()
#
# for i in threads:
#     i.join()
# print(common_list)

class MyThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        sleep(randint(0, 5))
        common_list.append(self.n)


threads = []
for i in range(20):
    th = MyThread(i)
    threads.append(th)
    th.start()
for i in threads:
    i.join()
print(common_list)
