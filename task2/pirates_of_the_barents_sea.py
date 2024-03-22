# Вася играет в настольную игру «Пираты Баренцева моря», которая посвящена
# морским битвам. Игровое поле представляет собой квадрат из N×N клеток,
# на котором расположено N кораблей (каждый корабль занимает одну клетку).
# Вася решил воспользоваться линейной тактикой, для этого ему необходимо
# выстроить все N кораблей в одном столбце. За один ход можно передвинуть
# один корабль в одну из четырёх соседних по стороне клеток. Номер столбца,
# в котором будут выстроены корабли, не важен. Определите минимальное
# количество ходов, необходимых для построения кораблей в одном столбце.
# В начале и процессе игры никакие два корабля не могут находиться в одной
# клетке.
def pirats(n: int, ships: list[list[int]]) -> int:
    ships.sort(key=lambda elem: elem[0])
    max_steps = float("inf")
    for i in range(n):
        curr_steps = 0
        for j in range(n):
            curr_steps += (abs(ships[j][1] - (i+1)) + abs(ships[j][0] - (j+1)))
        if curr_steps < max_steps:
            max_steps = curr_steps

    return max_steps


if __name__ == "__main__":
    with open(
        "/home/grivvus/Py_Projects/YoungYandex/algo_training_5/task2/input.txt"
    ) as file:
        n = int(file.readline())
        ships = []
        for i in range(n):
            ships.append([int(i) for i in file.readline().split()])
        print(pirats(n, ships))
