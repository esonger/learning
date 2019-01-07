# -*- coding: utf-8 -*-

# 查找一个最大子数组

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
def max_subarray(nums, low, high):
    if low == high:
        return low, high + 1, nums[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = max_subarray(nums, low, mid)
        right_low, right_high, right_sum = max_subarray(nums, mid + 1, high)
        cross_left_sum = -float('inf')
        total = 0
        cross_low = mid
        for i in range(mid, low - 1, -1):
            total += nums[i]
            if total > cross_left_sum:
                cross_left_sum = total
                cross_low = i

        cross_rigth_sum = -float('inf')
        total = 0
        cross_high = mid + 1
        for j in range(mid + 1, high + 1):
            total += nums[j]
            if total > cross_rigth_sum:
                cross_rigth_sum = total
                cross_high = j
        cross_sum = cross_left_sum + cross_rigth_sum

        if left_sum >= right_sum and left_sum >= cross_sum:
            return low, mid + 1, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return mid + 1, high + 1, right_sum
        else:
            return cross_low, cross_high+1, cross_sum


def find_max_subarray2(lists):
    if not lists:
        return lists
    low, high, _sum = max_subarray(lists, 0, len(lists)-1)
    return lists[low:high]


if __name__ == '__main__':
    l = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(l)
    print(find_max_subarray1(l))
    print(find_max_subarray2(l))
    l = [-2, 2, -3, 4, -1, 2, 1, -5, 3]
    print(l)
    print(find_max_subarray1(l))
    print(find_max_subarray2(l))
    l = []
    print(l)
    print(find_max_subarray1(l))
    print(find_max_subarray2(l))
    l = [-1, 5, 6, 9, 10, -9, -8, 100, -200]
    print(l)
    print(find_max_subarray1(l))
    print(find_max_subarray2(l))

