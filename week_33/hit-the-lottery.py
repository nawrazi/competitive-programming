# https://codeforces.com/gym/396349/problem/A

cash = int(input())
bills = [1, 5, 10, 20, 100]

total = 0
i = 4
while i > 0:
    if cash >= bills[i]:
        total += cash // bills[i]
        cash %= bills[i]
    i -= 1

print(total + cash)
