# Раунд плей-офф между двумя командами состоит из двух матчей.
# Каждая команда проводит по одному матчу «дома» и «в гостях».
# Выигрывает команда, забившая большее число мячей. Если же число забитых мячей
# совпадает, выигрывает команд, забившая больше мячей «в гостях».
# Если и это число мячей совпадает, матч переходит в дополнительный
# тайм или серию пенальти.

# Вам дан счёт первого матча, а также счёт текущей игры
# (которая ещё не завершилась).
# Помогите комментатору сообщить, сколько голов необходимо забить первой
# команде, чтобы победить, не переводя игру в дополнительное время.

def number_of_goals(m1: list[int], m2: list[int], f: int) -> int:
    first_team_score = m1[0] + m2[0]
    second_team_score = m1[1] + m2[1]
    diff = second_team_score - first_team_score
    if diff < 0:
        return 0

    if f == 2:
        if m1[0] > m2[1]:
            return diff
        else:
            return diff + 1
    else:
        if diff + m2[0] > m1[1]:
            return diff
        else:
            return diff + 1


if __name__ == "__main__":
    # m1 = [int(i) for i in input().split(":")]
    # m2 = [int(i) for i in input().split(":")]
    # flag = int(input())
    # print(number_of_goals(m1, m2, flag))
    print(number_of_goals([1, 2], [0, 3], 1))
    print(number_of_goals([0, 2], [0, 3], 1))
    print(number_of_goals([0, 2], [0, 3], 2))
    print(number_of_goals([1, 2], [2, 3], 1))
