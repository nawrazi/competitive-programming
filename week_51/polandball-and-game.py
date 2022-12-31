p, e = [int(i) for i in input().split()]
poland, enemy, common = set(), set(), set()

for _ in range(p):
    poland.add(input())
    
for _ in range(e):
    word = input()
    if word in poland:
        poland.remove(word)
        common.add(word)
    else:
        enemy.add(word)
        
if len(common) % 2 == 0:
    # poland
    if len(enemy) >= len(poland):
        print('NO')
    else:
        print('YES')
else:
    # enemy
    if len(poland) >= len(enemy):
        print('YES')
    else:
        print('NO')
        
