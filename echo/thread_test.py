# -*- coding: utf-8 -*-

import time
import threading

lock = threading.Lock()

def a(lock):
    while True:
        lock.acquire()
        print('lock one',)
        lock.acquire()
        print('lock two',)

def b(lock):
    while True:
        time.sleep(1)
        lock.release()
        print('lock release',)


threading.Thread(target=a, args=(lock,)).start()
threading.Thread(target=b, args=(lock,)).start()