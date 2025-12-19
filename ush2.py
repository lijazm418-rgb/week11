name=input("enter the student name")
score=int(input("enter the test score 0-50"))
if score>=40:
    print("A and pass")
    grade="A"
    result="pass"
elif score>=30:
    print("B and pass")
    grade="B"
    result="pass"
elif score>=20:
    print("C and pass")
    grade="C"
    result="pass"
else:
    print("failed")
    grade="D"
    result="failed"

