def bmi(kg,m):
    bmi = kg/((m/100)**2)
    return bmi

def comparebmi(kg,m):
    bmi = kg/((m/100)**2)

    if(bmi < 18.50):
        print("น้ำหนักน้อย/ผอม")
    elif(bmi >= 18.50 and bmi <= 22.90):
        print("ปกติ (สุขภาพดี)")
    elif(bmi >= 23 and bmi <= 24.90):
        print("ท้วม / โรคอ้วนระดับ 1")
    elif(bmi >= 25 and bmi <= 29.90):
        print("อ้วน / โรคอ้วนระดับ 2")
    else:
        print("อ้วนมาก / โรคอ้วนระดับ 3")
        
kg = int(input("รับค่าน้ำหนัก = "))
m = int(input("รับค่าส่วนสูง = "))
print("ดัชนีมวลกายของท่าน = %d" % bmi(kg,m))
comparebmi(kg,m)
