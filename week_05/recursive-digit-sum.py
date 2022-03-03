# https://www.hackerrank.com/challenges/recursive-digit-sum/problem

def superDigit(n, k, first):
    digit_sum = 0
    n = int(n)
    while n>0:
        digit_sum += n%10
        n = n//10

    if first and digit_sum*k<10:
        return digit_sum

    elif not first and digit_sum<10:
        return digit_sum

    if first:
        return superDigit(str(digit_sum*k), k, False)
    else:
        return superDigit(str(digit_sum), k, False)
