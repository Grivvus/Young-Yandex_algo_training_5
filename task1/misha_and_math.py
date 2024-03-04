# Миша сидел на занятиях математики в Высшей школе экономики
# и решал следующую задачу: дано n целых чисел и нужно расставить
# между ними знаки + и × так, чтобы результат полученного арифметического
# выражения был нечётным (например, между числами 5, 7, 2, можно расставить
# арифметические знаки следующим образом: 5×7+2=37).
# Так как примеры становились все больше и больше, а Миша срочно убегает
# в гости, от вас требуется написать программу решающую данную задачу.

def make_not_even(n: int, nums: list[int]) -> str:
    res = nums[0]
    s = ["1"] * (n-1)
    for i in range(1, n):
        if res % 2 != 0 and nums[i] % 2 != 0:
            # print("x", end="")
            s[i-1] = "x"
            res *= nums[i]
        else:
            # print("+", end="")
            s[i-1] = "+"
            res += nums[i]
    # print()
    print(*s, sep="")

if __name__ == "__main__":
    # n = int(input())
    # nums = [int(i) for i in input().split()]
    with open("/home/grivvus/Py_Projects/YoungYandex/algo_training_5/task1/input.txt") as f:
        n = int(f.readline())
        nums = [int(i) for i in f.readline().split()]
        make_not_even(n, nums)
