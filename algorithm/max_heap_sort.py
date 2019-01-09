# -*- coding: utf-8 -*-

'''
最大堆
'''


def max_heapify(lists, index, size):
    '''
    堆化
    :param list:
    :param index:
    :return:
    '''
    left_child = index * 2
    right_child = index * 2 + 1
    largest = index
    if left_child < size and lists[left_child] > lists[index]:
        largest = left_child
    if right_child < size and lists[right_child] > lists[largest]:
        largest = right_child
    if index != largest:
        lists[index], lists[largest] = lists[largest], lists[index]
        max_heapify(lists, largest, size)


def build_max_heap(lists, size):
    '''
    建堆
    :return:
    '''
    lists_len = len(lists)
    for index in range((size - 1) // 2, -1, -1):
        max_heapify(lists, index, lists_len)
    return lists


def min_heapify(lists, index, size):
    left_child = index * 2
    right_child = index * 2 + 1
    least = index
    if left_child<size and lists[left_child]<lists[index]:
        least = left_child
    if right_child<size and lists[right_child]<lists[least]:
        least = right_child
    if least != index:
        lists[index], lists[least] = lists[least], lists[index]
        min_heapify(lists, least, size)

def build_min_heap(lists, size):
    lists_len = len(lists)
    for index in range((size-1)//2, -1, -1):
        min_heapify(lists, index, lists_len)
    return lists


def heap_sort(lists, reverse=False):
    if reverse:
        lists = build_min_heap(lists, len(lists))
        for index in range(len(lists), 0, -1):
            lists[0], lists[index - 1] = lists[index - 1], lists[0]
            min_heapify(lists, 0, index - 1)
    else:
        lists = build_max_heap(lists, len(lists))
        for index in range(len(lists), 0, -1):
            lists[0], lists[index - 1] = lists[index - 1], lists[0]
            max_heapify(lists, 0, index - 1)
    return lists


if __name__ == '__main__':
    l = [4, 56, 2, 2, 4, 3, 6, 1, ]
    print(l)
    print(build_max_heap(l, len(l)))
    print(heap_sort(l))
    print(heap_sort(l, reverse=True))
