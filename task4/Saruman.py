# Как известно, Саруман Радужный очень любит порядок. Поэтому все полки его
# войска стоят друг за другом, причем каждый следующий полк содержит количество
# орков не меньше, чем предыдущий.
# Перед тем как напасть на Хельмову Падь, Саруман решил провести несколько
# вылазок для разведки. Чтобы его отряды никто не заметил, он решил каждый раз
# отправлять несколько подряд идущих полков так, чтобы суммарное количество
# орков в них было равно определенному числу. Так как это всего лишь разведка,
# каждый полк после вылазки возвращается на свое место. Задачу выбрать нужные
# полки он поручил Гриме Змеиному Языку. А Грима не поскупится на
# вознаграждение, если вы ему поможете.
def num_of_regiments(regiments: list[int], condition: list[int]) -> int:
    sum_ = sum(regiments[len(regiments)-condition[0]:])
    if sum_ < condition[1]:
        return -1
    if len(regiments) < condition[0]:
        return -1

    l = 0
    r = len(regiments) - condition[0]
    while l != r:
        mid = (l + r) // 2
        sum_ = 0
        for i in range(mid, mid + condition[0]):
            sum_ += regiments[i]
        if sum_ < condition[1]:
            l = mid + 1
        else:
            r = mid

    check_sum = 0
    for i in range(l, l+condition[0]):
        check_sum += regiments[i]
        if check_sum > condition[1]:
            return -1
    if check_sum == condition[1]:
        return l + 1
    return -1


def main():
    with open(
        "/home/grivvus/Py_Projects/YoungYandex/algo_training_5/task4/input.txt"
    ) as file:
        nm = [int(i) for i in file.readline().split()]
        data = []
        regiments = [int(i) for i in file.readline().split()]
        for i in range(nm[1]):
            data.append([int(i) for i in file.readline().split()])
        ans = []
        for i in data:
            ans.append(num_of_regiments(regiments, i))
        print(*ans, sep="\n")

if __name__ == "__main__":
    main()
