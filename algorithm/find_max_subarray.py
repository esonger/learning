# -*- coding: utf-8 -*-

# 查找最大子数组

# 穷举查找
def find_max_subarray1(lists):
    max = 0
    start = 0
    end = 0
    length = len(lists)
    for i in range(0, length):
        for j in range(i + 1, length):
            sub_sum = sum(lists[i:j])
            if sub_sum > max:
                max = sub_sum
                start = i
                end = j
    return list(lists[start:end])

# 递归查找
# 寻找一个基准，则最大子数组可能存在的位置，1， 基准左侧。2， 基准右侧。3， 跨基准(左侧最大后缀+右侧最大前缀)
def find_max_subarray2(lists):
    pass


if __name__ == '__main__':
    l = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_max_subarray1(l))
