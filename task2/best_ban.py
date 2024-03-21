# Константин и Михаил играют в настольную игру «Ярость Эльфов». В игре есть
# n рас и m классов персонажей. Каждый персонаж характеризуется своими расой
# и классом. Для каждой расы и каждого класса существует ровно один персонаж
# такой расы и такого класса. Сила персонажа i-й расы и j-го класса равна
# a[i][j], и обоим игрокам это прекрасно известно.
# Сейчас Константин будет выбирать себе персонажа. Перед этим Михаил может
# запретить одну расу и один класс, чтобы Константин не мог выбирать
# персонажей, у которых такая раса или такой класс. Конечно же, Михаил
# старается, чтобы Константину достался как можно более слабый персонаж,
# а Константин, напротив, выбирает персонажа посильнее. Какие расу и класс
# следует запретить Михаилу?

def best_ban(n: int, m:int, chars: list[list[int]]) -> list[int]:
    mx1 = custom_max(chars, -1, -1)
    mx2 = custom_max(chars, mx1[1], -1)
    mx3 = custom_max(chars, -1, mx1[2])
    mx4 = custom_max(chars, mx1[1], mx2[2])
    mx5 = custom_max(chars, mx3[1], mx1[2])
    if mx4 < mx5:
        return [mx1[1] + 1, mx2[2] + 1]
    return [mx3[1] + 1, mx1[2] + 1]


def custom_max(data: list[list[int]], row_ban, col_ban) -> tuple[int]:
    res = 0
    row, col = 0, 0
    for i in range(len(data)):
        if i != row_ban:
            for j in range(len(data[i])):
                if j != col_ban:
                    if data[i][j] > res:
                        res = data[i][j]
                        row = i; col = j

    return res, row, col


if __name__ == "__main__":
    with open(
        "/home/grivvus/Py_Projects/YoungYandex/algo_training_5/task2/input.txt"
    ) as file:
        nm = [int(i) for i in file.readline().split()]
        chars = []
        for i in range(nm[0]):
            chars.append([int(i) for i in file.readline().split()])
        print(*best_ban(nm[0], nm[1], chars))
