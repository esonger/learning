# -*- coding: utf-8 -*-

# 插入排序

def cmp(a, b, reverse=False):
    if reverse:
        return a > b
    else:
        return a < b

def insert_sort(lists, reverse=False):
    length = len(lists)
    for index in range(1, length):
        key = lists[index]
        next = index - 1
        while cmp(key, lists[next], reverse):
            lists[next + 1] = lists[next]
            next -= 1
            if next < 0:
                break
        lists[next + 1] = key

    return lists


if __name__ == '__main__':
    l = []
    print(insert_sort(l))
    l = [4, 56, 2, 2, 4, 3, 6, 1, ]
    print(l)
    print(insert_sort(l))
    print(insert_sort(l, reverse=True))
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
    print(l)
    print(insert_sort(l))
    print(insert_sort(l, reverse=True))
