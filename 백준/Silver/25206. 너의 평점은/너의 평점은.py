import sys
input = sys.stdin.readline

grade_map = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}
credit_sum = 0
grade_sum = 0
for _ in range(20):
    subject, credit, grade = input().strip().split()
    if grade == 'P':
        continue
    else:
        credit_sum += float(credit)
        grade_sum += float(credit) * grade_map[grade]

print(grade_sum / credit_sum)