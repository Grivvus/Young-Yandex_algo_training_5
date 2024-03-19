# Вам даны три списка чисел. Найдите все числа, которые встречаются хотя бы
# в двух из трёх списков.
def atleast_in_two(l1: list[int], l2: list[int], l3: list[int]) -> list[int]:
    d = {}
    for i in list(set(l1)) + list(set(l2)) + list(set(l3)):
        if i not in d:
            d[i] = 0
        d[i] += 1

    ans = []
    for i in d.keys():
        if d[i] >= 2:
            ans.append(i)
    ans.sort()
    return ans


if __name__ == "__main__":
    n1 = int(input())
    l1 = [int(i) for i in input().split()]
    n2 = int(input())
    l2 = [int(i) for i in input().split()]
    n3 = int(input())
    l3 = [int(i) for i in input().split()]
    print(*atleast_in_two(l1, l2, l3))
