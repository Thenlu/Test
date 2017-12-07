#单线程
import time
# def say():
#     print("66600")
#
#     time.sleep(1)
#
# if __name__ == '__main__':
#     for i in range(0,5):
#         say()
'''
#多线程执行
import threading
def sry():
    print("7777")
    time.sleep(1)
if __name__ == '__main__':
    for i in range(4):
        t = threading.Thread(target=sry)
        t.start()
'''

# import threading
# from time import sleep,ctime
#
# def sing():
#     for i in range(3):
#         print("在唱歌%d"%i)
#         sleep(1)
# def dance():
#     for i in range(3):
#         print("正在跳舞%d"%i)
#         sleep(1)
# if __name__ == '__main__':
#     print("---开始---%s"%ctime())
#
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance)
#     t1.start()
#     t2.start()
#
#     # print('---结束%s'%ctime())
#     while True:
#         length = len(threading.enumerate())
#         print("当前的运行线程数wei %d"%length)
#
#         if length<=1:
#             break
#
#         sleep(0.5)
'''
import threading
import time
class Mythread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + 'xiancheng' + ' @ ' + str(i)
            print(msg)

if __name__ == '__main__':
    t = Mythread()
    t.start()
'''
from threading import Thread
import time
def work(nums):
    nums.append(44)
    print("----in work1---",nums)

def work2(nums):
    time.sleep(1)
    print("----in work2---",nums)
g_nums = [11,22,33]

t1 = Thread(target=work,args=(g_nums,))
t1.start()

t2 = Thread(target=work2,args=(g_nums,))
t2.start()
