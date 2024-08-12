n = int(input())

student_marks = {}  # dictionary
for _ in range(n):
    name, *line = input().split(" ")
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

for i in student_marks:
    if i == query_name:
        avg = sum(student_marks[i]) / len(student_marks[i])
        print("%.2f" % avg)
