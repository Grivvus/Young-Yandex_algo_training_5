# Дан массив целых положительных чисел a длины n. Разбейте его на минимально
# возможное количество отрезков, чтобы каждое число было не меньше длины
# отрезкакоторому оно принадлежит. Длиной отрезка считается количество чисел
# в нем.
# Разбиение массива на отрезки считается корректным, если каждый элемент
# принадлежит ровно одному отрезку.

def no_more_no_less(ln: int, arr: list[int]) -> list[int]:
    arrs: list[list] = []
    min_in_segment = float("inf")
    for i in arr:
        if not arrs:
            min_in_segment = i
            arrs.append([i])
        else:
            if min_in_segment > len(arrs[-1]) and i > len(arrs[-1]):
                arrs[-1].append(i)
                if i < min_in_segment:
                    min_in_segment = i
            else:
                min_in_segment = i
                arrs.append([i])

    answer: list = [len(arrs)]
    for i in arrs:
        answer.append(len(i))

    return answer

if __name__ == "__main__":
    with open(
        "input.txt"
    ) as file:
        n = int(file.readline())
        for i in range(n):
            ln = int(file.readline())
            arr = [int(i) for i in file.readline().split()]
            ans = no_more_no_less(ln, arr)
            print(ans[0])
            print(*ans[1:])
