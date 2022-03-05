def isGood(difficulty):
    median = (len(students) - 1) // 2

    too_hard = difficulty > students[median]
    too_easy = difficulty <= students[0]

    return not too_hard and not too_easy


def solve(students, questions):
    for difficulty in questions:
        good = isGood(difficulty)
        output = 'YES' if good else 'NO'
        print(output)


n, m = [int(i) for i in input().split()]
students = sorted([int(n) for n in input().split()])
questions = []
for _ in range(n):
    questions.append(int(input()))

solve(students, questions)
