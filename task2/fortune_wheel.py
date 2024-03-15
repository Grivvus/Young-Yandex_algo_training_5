# Развлекательный телеканал транслирует шоу «Колесо Фортуны». В процессе игры
# участники шоу крутят большое колесо, разделенное на сектора. В каждом секторе
# этого колеса записано число. После того как колесо останавливается,
# специальная стрелка указывает на один из секторов. Число в этом секторе
# определяет выигрыш игрока.
# Юный участник шоу заметил, что колесо в процессе вращения замедляется из-за
# того, что стрелка задевает за выступы на колесе, находящиеся между секторами.
# Если колесо вращается с угловой скоростью v градусов в секунду, и стрелка,
# переходя из сектора X к следующему сектору, задевает за очередной выступ, то
# текущая угловая скорость движения колеса уменьшается на k градусов в секунду.
# При этом если v ≤ k, то колесо не может преодолеть препятствие и
# останавливается. Стрелка в этом случае будет указывать на сектор X.
# Юный участник шоу собирается вращать колесо. Зная порядок секторов на колесе,
# он хочет заставить колесо вращаться с такой начальной скоростью, чтобы после
# остановки колеса стрелка указала на как можно большее число. Колесо можно
# вращать в любом направлении и придавать ему начальную угловую скорость от a
# до b градусов в секунду.
# Требуется написать программу, которая по заданному расположению чисел в
# секторах, минимальной и максимальной начальной угловой скорости вращения
# колеса и величине замедления колеса при переходе через границу секторов
# вычисляет максимальный выигрыш.
def fortune_wheel(n: int, sectors: list[int], abk: list[int]) -> int:
    max_el = -1
    i1 = abk[0] // abk[2] if abk[0]%abk[2] else abk[0] // abk[2] - 1
    i2 = abk[1] // abk[2] if abk[1]%abk[2] else abk[1] // abk[2] - 1
    if i2 - i1 >= n:
        return max(sectors)
    max_el1 = max(sectors[i1%n:i1%n+(i2-i1)+1])
    sectors = [sectors[0]] + sectors[::-1][:-1]
    max_el2 =  max(sectors[i1%n:i1%n+(i2-i1)+1])
    max_el = max_el1 if max_el1 > max_el2 else max_el2
    return max_el


if __name__ == "__main__":
    with open(
        "/home/grivvus/Py_Projects/YoungYandex/algo_training_5/task2/input.txt"
    ) as file:
        n = int(file.readline())
        sect = [int(i) for i in file.readline().split()]
        abk = [int(i) for i in file.readline().split()]
        print(fortune_wheel(n, sect, abk))
