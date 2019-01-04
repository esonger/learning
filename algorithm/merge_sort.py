# -*- coding: utf-8 -*-

# 归并排序

def cmp(a, b, reverse=False):
    if reverse:
        return a > b
    else:
        return a < b

def merge(left, right, reverse=False):
    result = []
    while len(left) > 0 and len(right) > 0:
        if cmp(left[0], right[0], reverse):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right

    return result


def merge_sort(lists, reverse=False):
    if len(lists) <= 1:
        return lists
    left = merge_sort(lists[:len(lists) // 2], reverse=reverse)
    right = merge_sort(lists[len(lists) // 2:], reverse=reverse)
    return merge(left, right, reverse=reverse)


if __name__ == '__main__':
    l = []
    print(merge_sort(l))
    l = [4, 56, 2, 2, 4, 3, 6, 1, ]
    print(l)
    print(merge_sort(l))
    print(merge_sort(l, reverse=True))
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
    print(l)
    print(merge_sort(l))
    print(merge_sort(l, reverse=True))
