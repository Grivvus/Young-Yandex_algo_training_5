def find_max_profit(price, k):
    max_profit = 0
    min_price_k_back = [price[0], 0]
    i = 1
    while i < len(price):
        if i - min_price_k_back[1] > k:
            min_price_k_back = [
                price[min_price_k_back[1]+1], min_price_k_back[1]+1
            ]
            i = min_price_k_back[1] + 1
        if  price[i] - min_price_k_back[0] > max_profit:
            max_profit = price[i] - min_price_k_back[0]
        if price[i] < min_price_k_back[0]:
            min_price_k_back = [price[i], i]
        i += 1
    return max_profit

if __name__ == "__main__":
    nk = [int(i) for i in input().split()]
    price = [int(i) for i in input().split()]
    print(find_max_profit(price, nk[1]))
