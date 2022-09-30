# https://codeforces.com/gym/401249/problem/D

def getPrimes(n):
    prime = [True for _ in range(n)]

    num = 2
    while num * num <= n - 1:
        if prime[num]:
            for mult in range(num * num, n, num):
                prime[mult] = False
        num += 1

    return [i + 2 for i, p in enumerate(prime[2:]) if p]

n = int(input())
nums = [int(n) for n in input().split()]
ones = nums.count(1)
twos = nums.count(2)
primes = getPrimes(n + 1)

if not primes:
    print(*nums)
    exit()

nex_prime = 0
cur_pre = 0
ans = []
for _ in range(n):
    if primes[nex_prime] - cur_pre == 2:
        if twos >= 1:
            cur_pre += 2
            twos -= 1
            ans.append(2)
        elif ones >= 2:
            cur_pre += 2
            ones -= 2
            ans.append(1)
            ans.append(1)
        else:
            break

    elif primes[nex_prime] - cur_pre == 1:
        if ones >= 1:
            cur_pre += 1
            ones -= 1
            ans.append(1)
        elif twos >= 1:
            cur_pre += 2
            twos -= 1
            ans.append(2)
        else:
            break

    else:
        if twos >= 1:
            cur_pre += 2
            twos -= 1
            ans.append(2)
        elif ones >= 1:
            cur_pre += 1
            ones -= 1
            ans.append(1)
        else:
            break

    nex_prime += 1

    if nex_prime >= len(primes):
        break

while twos > 0:
    ans.append(2)
    twos -= 1

while ones > 0:
    ans.append(1)
    ones -= 1

print(*ans)
