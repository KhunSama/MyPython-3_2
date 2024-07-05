def beforeMidterm(a,b,c):
    total = a+b+c
    return total

score = int(input("คะแนนเก็บ: "))
points = int(input("คะแนนจิตพิสัย: "))
midterm = int(input("คะแนนกลางภาค: "))
print("คะแนนรวม: ", beforeMidterm(score,points,midterm))