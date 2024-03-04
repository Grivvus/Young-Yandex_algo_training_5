# k друзей организовали стартап по производству укулеле для кошек.
# На сегодняшний день прибыль составила n рублей. Вы, как главный бухгалтер
# компании, хотите в каждый из ближайших d дней приписывать по одной
# цифре в конец числа, выражающего прибыль. При этом в каждый из дней прибыль
# должна делиться на k.

def get_number(data: list[int]) -> int:
    num_str = str(data[0])
    start_len = len(num_str)
    for i in range(10):
        if int(num_str + str(i)) % data[1] == 0:
            num_str += str(i)
            break
    if len(num_str) == start_len:
        return -1
    good_num = int(num_str)
    good_num *= (10**(data[2]-1))
    return good_num


if __name__ == "__main__":
    import sys
    sys.set_int_max_str_digits(10**9)
    data = [1000000000, 1000000000, 100000]
    print(get_number(data))

