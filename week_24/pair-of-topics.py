l = int(input())
teach = [int(i) for i in input().split()]
stud = [int(i) for i in input().split()]

sums = sorted([t - s for t, s in zip(teach, stud)])

print([t - s for t, s in zip(teach, stud)])
print(sums)

i = 0
while i < l:
    if sums[i] + sums[0] >= 0:
        break
    i += 1

total = (l * (l - 1) // 2) - (i * (i - 1) // 2)

print(total)