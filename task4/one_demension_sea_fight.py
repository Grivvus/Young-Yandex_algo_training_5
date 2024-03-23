# Поле в игре в одномерный морской бой имеет размеры 1×n. Ваша задача —
# найти такое максимальное k, что на поле можно расставить один корабль размера
# 1×k, два корабля размера 1×(k−1), …, k кораблей размера 1×1, причем корабли,
# как и в обычном морском бое, не должны касаться друг друга и пересекаться.
def sea_fight(n: int) -> int:
    r = n
    l = 0
    while l != r:
        mid = (r + l + 1) // 2
        sm = 0
        for i in range(1, mid+1):
            sm += (i * (mid - i + 1))
            sm += (mid - i + 1)
            if sm - 1 > n:
                break
        sm -= 1
        if sm <= n:
            l = mid
        else:
            r = mid - 1

    return l

def main():
    n = int(input())
    print(sea_fight(n))


if __name__ == "__main__":
    main()