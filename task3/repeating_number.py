# Вам дана последовательность измерений некоторой величины. Требуется
# определить, повторялась ли какое-либо число, причём расстояние между
# повторами не превосходило k.

def repeating_number(n: int, k: int, nums: list[int]) -> bool:
    d = {}
    for i in range(n):
        if nums[i] not in d:
            d[nums[i]] = i
        else:
            if i - d[nums[i]] <= k:
                return True
            else:
                d[nums[i]] = i

    return False

if __name__ == "__main__":
    nk = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    print("YES") if repeating_number(nk[0], nk[1], nums) else print("NO")
