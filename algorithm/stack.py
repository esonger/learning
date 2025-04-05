# -*- coding: utf-8 -*-
'''
栈结构的实现及操作
'''


class Node(object):
    def __init__(self, _next, value):
        self.value = value
        self._next = _next


class Stack(object):

    def __init__(self):
        self._top = None
        self.length = 0

    def is_empty(self):
        if self._top is None:
            return True
        return False

    def top(self):
        '''
        查看栈顶元素
        :return:
        '''
        if self.is_empty():
            return None
        return self._top.value

    def pop(self):
        '''
        出栈
        :return:
        '''
        if self.is_empty():
            raise Exception
        node = self._top
        self._top = self._top._next
        self.length -= 1
        return node.value

    def push(self, ele):
        '''
        入栈
        :param ele:
        :return:
        '''
        node = Node(_next=self._top, value=ele)
        self._top = node
        self.length += 1

    def __len__(self):
        return self.length


if __name__ == '__main__':
    stack = Stack()
    for item in range(10):
        stack.push(item)
    print(len(stack))
    print(stack.top())
    print(stack.pop())
    print(len(stack))