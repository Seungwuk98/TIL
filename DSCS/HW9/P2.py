def P2(stock_price: list) -> list:
    ##### Write your Code Here #####
    s = []
    n = len(stock_price)
    ret = [0]*n
    for i in range(n):
        while s and s[-1][0] < stock_price[i]:
            price, day = s.pop()
            ret[day] = i-day
        s.append((stock_price[i], i))
    return ret
    ##### End of your code #####
