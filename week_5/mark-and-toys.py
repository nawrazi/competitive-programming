# https://www.hackerrank.com/challenges/mark-and-toys/problem

def maximumToys(prices, k):
    items = 0
    prices.sort()
    for price in prices:
        if k<=0:
            return items-1
        k-=price
        items+=1

    return items if k==0 else items-1
