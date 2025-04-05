# -*- coding: utf-8 -*-

'''
快速排序
'''


def partition(lists, start, end):
    '''
    处理lists，并找到一个索引位置i，使该位置左侧的元素<=lists[i]<=右侧元素
    '''

    i = start - 1
    for index in range(start, end):
        if lists[index] < lists[end]:
            i += 1
            lists[i], lists[index] = lists[index], lists[i]
    lists[i + 1], lists[end] = lists[end], lists[i + 1]
    return i + 1


def quick_sort(lists, start, end):
    if start < end:
        q = partition(lists, start, end)
        quick_sort(lists, start, q - 1)
        quick_sort(lists, q + 1, end)
    return lists


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
    print(l)
    print(quick_sort(l, 0, len(l) - 1))
    l = [4, 56, 2, 2, 4, 3, 6, 1, ]
    print(l)
    print(quick_sort(l, 0, len(l) - 1))
    l = []
    print(quick_sort(l, 0, len(l) - 1))
    l = [4, 56, 2, 2, 4, 3, 6, 1, 2, 56, 4]
    print(l)
    print(quick_sort(l, 0, len(l) - 1))
