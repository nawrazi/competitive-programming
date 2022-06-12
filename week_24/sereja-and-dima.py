from collections import deque

_ = input()
cards = deque([int(i) for i in input().split()])

score = [0, 0]
turn = 0

while cards:
    if cards[0] >= cards[-1]:
        score[turn] += cards.popleft()
    else:
        score[turn] += cards.pop()

    turn = abs(turn - 1)

print(*score)
