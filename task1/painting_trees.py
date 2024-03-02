# Вася и Маша участвуют в субботнике и красят стволы деревьев в белый цвет.
# Деревья растут вдоль улицы через равные промежутки в 1 метр.
# Одно из деревьев обозначено числом ноль,
# деревья по одну сторону занумерованы положительными числами 1,2 и т.д.,
# а в другую — отрицательными −1,−2 и т.д.

# Ведро с краской для Васи установили возле дерева P, а для Маши — возле дерева Q.
# Ведра с краской очень тяжелые и Вася с Машей не могут их переставить,
# поэтому они окунают кисть в ведро и уже с этой кистью идут красить дерево.
# Краска на кисти из ведра Васи засыхает, когда он удаляется от ведра более чем
# на V метров, а из ведра Маши — на M метров. Определите, сколько деревьев
# может быть покрашено.

def count_trees(petya: list[int], masha: list[int]) -> int:
    n_t_all: set = set()

    for i in range(petya[0], petya[0]+petya[1]+1, 1):
        n_t_all.add(i)
    for i in range(petya[0], petya[0]-petya[1]-1, -1):
        n_t_all.add(i)

    for i in range(masha[0], masha[0]+masha[1]+1, 1):
        n_t_all.add(i)
    for i in range(masha[0], masha[0]-masha[1]-1, -1):
        n_t_all.add(i)

    return len(n_t_all)


def count_trees_fast(petya: list[int], masha: list[int]) -> int:
    left_p = petya[0] - petya[1]
    right_p = petya[0] + petya[1]
    left_m = masha[0] - masha[1]
    right_m = masha[0] + masha[1]
    if ((right_m <= right_p and left_m >= left_p) or
        (right_m >= right_p and left_m <= left_p)):
        print("if")
        return abs(max(right_p, right_m) - min(left_m, left_p)) + 1
    elif right_m < left_p or right_p < left_m:
        print("elif")
        return (abs(min(right_m, right_p) - min(left_p, left_m))
                + abs(max(right_m, right_p) - max(left_m, left_p)) + 2)
    else:
        print("else")
        return abs(max(right_m, right_p) - min(left_p, left_m)) + 1
    # else:
    #     print(petya)
    #     print(masha)
    #     raise RuntimeError()


if __name__ == "__main__":
    p = [int(i) for i in input().split()]
    m = [int(i) for i in input().split()]
    print(count_trees_fast(p, m))

    # import random
    # while True:
    #     p = [random.randint(-(10**2), 10**2), random.randint(0, 10**2)]
    #     m = [random.randint(-(10**2), 10**2), random.randint(0, 10**2)]
    #     right_res = count_trees(p, m)
    #     wtf_res = count_trees_fast(p, m)
    #     if (wtf_res != right_res):
    #         print(p, m)
    #         print(right_res)
    #         print(wtf_res)
    #         break