def checker(string):
    length = len(string)
    i, j = 0, 1
    map = { string[i]: True }
    mySet = set()

    while j<length:
        if string[j] not in map:
            map[string[j]] = True
            # print(111)

        elif string[j] in map and map[string[j]]==False:
            map[string[j]] = True
            mySet.add(string[j])
            # print(333)

        elif string[j]==string[i]:
            # print(string[j], '**')
            if string[j] not in mySet:
                map[string[j]] = False
                # print(222)

        elif string[j] in map and string[i]!=string[j]:
            map[string[j]] = True
            mySet.add(string[j])

        i+=1
        j+=1
        # print(map)

    temp_string = ''
    for letter in sorted(map):
        if map[letter]==True:
            temp_string+=letter
    res.append(temp_string)


t = int(input())
res = []
for _ in range(t):
    string = input()
    checker(string)

for s in res:
    print(s)
