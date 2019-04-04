# -*- coding: utf-8 -*-
'''
数据结构： 队列，线程不安全
'''

class Node(object):
    def __init__(self, value):
        self.next = None
        self.value = value

class Queue(object):
    def __init__(self):
        pass

    def is_empty(self):
        pass

    def en_queue(self, value):
        pass

    def de_queue(self):
        pass

    def __len__(self):
        pass

if __name__ == '__main__':
    q = Queue()