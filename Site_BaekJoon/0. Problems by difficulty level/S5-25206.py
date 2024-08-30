import sys
sys.stdin = open("input.txt", "r")

hash_grade = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0.0, "P" : 0.0}

total_credit = 0
total_grade = 0

for i in range (20):
    s = input().split()
    credit, grade = s[1], s[2]
    total_credit += float(credit)
    if grade != "P":
        total_grade += float(credit) * hash_grade[grade]
    else:
        total_credit -= float(credit)

print("%.6f" % (total_grade / total_credit))