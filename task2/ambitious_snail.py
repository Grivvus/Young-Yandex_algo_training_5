# Домашний питомец мальчика Васи — улитка Петя. Петя обитает на бесконечном
# в обе стороны вертикальном столбе, который для удобства можно представить
# как числовую прямую. Изначально Петя находится в точке 0.
# Вася кормит Петю ягодами. У него есть n ягод, каждая в единственном
# экземпляре.Вася знает, что если утром он даст Пете ягоду с номером i,
# то поев и набравшись сил, за остаток дня Петя поднимется на ai единиц вверх
# по столбу, но при этом за ночь, потяжелев, съедет на bi единиц вниз.
# Параметры различных ягод могут совпадать.
# Пете стало интересно, а как оно там, наверху, и Вася взялся ему в этом помочь.
# Ближайшие n дней он будет кормить Петю ягодами из своего запаса таким образом,
# чтобы максимальная высота, на которой побывал Петя за эти n дней была
# максимальной. К сожалению, Вася не умеет программировать, поэтому он
# попросил вас о помощи. Найдите, максимальную высоту, на которой Петя сможет
# побывать за эти n дней и в каком порядке Вася должен давать Пете ягоды,
# чтобы Петя смог её достичь!
def calc_max_height(barries: list[int]) -> int:
    max_height = 0
    current_height = 0
    indexes = []
    for i in barries:
        current_height += i[0]
        if current_height > max_height:
            max_height = current_height
        current_height -= i[1]
        indexes.append(i[2])
    return (max_height, indexes)


if __name__ == "__main__":
    barries_pos = []
    barries_oth = []
    max_fall = [0, -1]
    max_raise = [0, -1]
    with open(
        "/home/grivvus/Py_Projects/YoungYandex/algo_training_5/task2/input.txt"
    ) as file:
        n = int(file.readline())
        for i in range(n):
            curr = [int(i) for i in file.readline().split()]
            curr.append(i+1)
            if curr[0] - curr[1] > 0:
                if curr[1] > max_fall[0]:
                    max_fall = [curr[1], len(barries_pos)]
                barries_pos.append(curr)
            else:
                if curr[0] > max_raise[0]:
                    max_raise = [curr[0], len(barries_oth)]
                barries_oth.append(curr)
    if max_raise[0] > max_fall[0]:
        key_elem = barries_oth.pop(max_raise[1])
    else:
        key_elem = barries_pos.pop(max_fall[1])
    res = calc_max_height(barries_pos + [key_elem] + barries_oth)
    print(res[0])
    print(*res[1])