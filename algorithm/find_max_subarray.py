# -*- coding: utf-8 -*-

# 查找最大子数组


def find_max_subarray1(lists):
    # 暴力查找
    max = 0
    start = 0
    end = 0
    print(lists)
    for i in range(0, len(lists)):
        for j in range(i + 1, len(lists)):
            sub_sum = sum(lists[i:j])
            if sub_sum > max:
                max = sub_sum
                start = i
                end = j
    return list(lists[start:end])


if __name__ == '__main__':
    l = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_max_subarray1(l))
