import sys

coins = sys.stdin.readlines()
cache = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11}

def exchange_coin(coin):

    if coin not in cache:
        value = exchange_coin(coin//2) + exchange_coin(coin//3) + exchange_coin(coin//4)
        if value < coin:
            value = coin
        cache[coin] = value
        return value
    else:
        return cache[coin]

for coin in coins:
    print(exchange_coin(int(coin)))