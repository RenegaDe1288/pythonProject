import random


def change(nums1):
    nums = list(nums1)
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    nums[index] = value
    return nums, value


my_nums = 1, 2, 3, 4, 5
new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)

new_nums2, rand_val2 = change(new_nums)
print(new_nums2, rand_val2)

rand_val += rand_val2
print(rand_val)
