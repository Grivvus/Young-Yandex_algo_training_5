# Дан массив a из n чисел. Найдите минимальное количество чисел, после
# удаления которых попарная разность оставшихся чисел по модулю не будет
# превышать 1, то есть после удаления ни одно число не должно отличаться
# от какого-либо другого более чем на 1.
def deleting_number(n: int, nums: list[int]) -> int:
    if n == 1:
        return 0
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 0
        d[i] += 1

    keys_ = list(d.keys())
    keys_.sort()
    max_sum = 0
    for i in range(len(keys_)):
        curr_sum = d[keys_[i]]
        if keys_[i] - keys_[i-1] == 1:
            curr_sum += d[keys_[i-1]]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return n - max_sum


if __name__ == "__main__":
    n = int(input())
    nums = [int(i) for i in input().split()]
    print(deleting_number(n, nums))
