# н массив из N целых чисел. Все числа от −10**9 до 10**9.
# Нужно уметь отвечать на запросы вида “Cколько чисел имеют значения отL до R?"

def find_min_pos(nums: list[int], min_num: int) -> int:
    l = 0
    r = len(nums) - 1
    while l != r:
        mid = (l+r) // 2
        if nums[mid] >= min_num:
            r = mid
        else:
            l = mid + 1
    return l

def find_max_pos(nums: list[int], max_num) -> int:
    l = 0
    r = len(nums) - 1
    while l != r:
        mid = (l+r+1) // 2
        if nums[mid] <= max_num:
            l = mid
        else:
            r = mid - 1
    return l


def numbers_between(nums: list[int], min_num: int, max_num: int) -> int:
    if len(nums) == 1 and nums[0] in range(min_num, max_num +1):
        return 1
    elif len(nums) == 1:
        return 0
    if min_num > nums[-1] or max_num < nums[0]:
        return 0
    left_border = find_min_pos(nums, min_num)
    right_border = find_max_pos(nums, max_num)
    return right_border - left_border + 1


def main():
    with open(
        "/home/grivvus/Py_Projects/YoungYandex/algo_training_5/task4/input.txt"
    ) as file:
        n = int(file.readline())
        nums = [int(i) for i in file.readline().split()]
        nums.sort()
        k = int(file.readline())
        for i in range(k):
            pair = [int(i) for i in file.readline().split()]
            print(numbers_between(nums, pair[0], pair[1]), end=" ")


if __name__ == "__main__":
    main()

