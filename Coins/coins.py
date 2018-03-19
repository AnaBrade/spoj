import sys

coins = sys.stdin.readlines()
cache = {}

def exchange_coin(coin):

    if coin not in cache:
        if coin > 11:
            value1 = exchange_coin(coin//2)
            value2 = exchange_coin(coin//3)
            value3 = exchange_coin(coin//4)

            if (value1+value2+value3) > coin:
                cache[coin] = value1 + value2 + value3
                return value1 + value2 + value3
            else:
                cache[coin] = coin
                return coin
        else:
            cache[coin] = coin
            return coin
    else:
        return cache[coin]

for coin in coins:
    print(exchange_coin(int(coin)))