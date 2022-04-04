# https://www.hackerrank.com/contests/a2sv3-contest-3/challenges/sherlock-and-squares

def squares(a, b):
    squares = math.floor(math.sqrt(b)) - math.floor(math.sqrt(a))
    extra = int(math.ceil(math.sqrt(a) - math.floor(math.sqrt(a))) == 0)

    return squares + extra
