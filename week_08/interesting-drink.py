def searchForAffordables(budget, prices):
    start, end = 0, len(prices)-1
    best = 0

    while start<=end:
        mid = (start+end)//2

        if prices[mid] <= budget:
            best = mid+1
            start = mid+1
        else:
            end = mid-1

    return best


def calculate(prices, budgets):
    for budget in budgets:
        affordables = searchForAffordables(budget,prices)
        print(affordables)



n = int(input())
prices = [int(n) for n in input().split()]
m = int(input())
budgets = []
for _ in range(m):
    budgets.append(int(input()))

calculate(sorted(prices), budgets)
