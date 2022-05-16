def solve(s1, s2):
    initial = [len(s1), len(s2)]
    same = 0
    while s1 and s2 and s1[-1] == s2[-1]:
        s1.pop()
        s2.pop()
        same += 1

    print(initial[0] + initial[1] - 2 * same)


word1 = input()
word2 = input()
solve(list(word1), list(word2))