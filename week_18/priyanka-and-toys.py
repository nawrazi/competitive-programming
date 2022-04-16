# https://www.hackerrank.com/contests/a2sv3-contest-8/challenges/priyanka-and-toys

def toys(weights):
    weights.sort()
    conts = 1
    cur_min = weights[0]
    for weight in weights:
        if weight > cur_min + 4:
            cur_min = weight
            conts += 1

    return conts
