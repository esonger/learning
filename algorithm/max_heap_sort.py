# -*- coding: utf-8 -*-

'''
最大堆
'''


def max_heapify(lists, index):
    '''
    堆化
    :param list:
    :param index:
    :return:
    '''
    left_child = index * 2
    right_child = index * 2 + 1
    lists_len = len(lists)
    largest = index
    if left_child < lists_len and lists[left_child] > lists[index]:
        largest = left_child
    if right_child < lists_len and lists[right_child] > lists[largest]:
        largest = right_child
    if index != largest:
        lists[index], lists[largest] = lists[largest], lists[index]
        max_heapify(lists, largest)

def build_max_heap(lists, size):
    '''
    建堆
    :return:
    '''

    for index in range((size-1)//2, -1, -1):
        max_heapify(lists, index)
    return lists

def heap_sort(lists, reverse=False):
    lists = build_max_heap(lists, len(lists))
    for index in range(len(lists)):
        pass



if __name__ == '__main__':
    l = [4, 56, 2, 2, 4, 3, 6, 1, ]
    print(l)
    print(build_max_heap(l, len(l)))