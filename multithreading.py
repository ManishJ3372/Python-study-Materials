#ohy,what.how
#multi-threading(multi-tasking)-->executing several task simultaneously

#1.creating a thread without using class
#2.create a thread by extending thread class

#daemon thread
#the thread which is running un the background are called daemon thread
#the main objective of daemon thread is to provide support for non daemon thread(like main thread)

#eg:-

# from threading import *
# import threading
#
# print(currentThread().isDaemon())
# print(threading.currentThread().getName())

#syntax==>
# import threading
# print(threading.currentThread().getName())

# from threading import *
# import time
# def wish(name):
#     for i in range(1,11):
#         print("Good Morning",end=" ")
#         time.sleep(2)
#         print(name)
# t=Thread(target=wish("manish"))
# t.start()
# t.start()

#we can change daemon nature by using setdaemon() method class.
#syntax==>t,setDaemon(true)
#eg:-

#from threading import *
# def job():
#     print("child")
# t1=Thread(target=job())
# print(t1.IsDaemon())
# t1.setDaemon(True)
# print(t1.IsDaemon())


from threading import *
import time
def job():
    for i in range(1.6):
        print("child thread")
        time.sleep(2)
t1=Thread(target=job())
print(t1.isDaemon())
t1.setDaemon(True)
print(t1.setDaemon())
t1.start()
time.sleep(s)
print("end of main thread")
