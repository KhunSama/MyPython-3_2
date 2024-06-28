num = int(input("ป้อนค่าคะแนน: "))
if 80 <= num <= 100:
    print("เกรด A")
elif 70 <= num <= 79:
    print("เกรด B")
elif 60 <= num <= 69:
    print("เกรด C")
elif 50 <= num <= 59:
    print("เกรด D")
elif 40 <= num <= 49:
    print("เกรด F")
elif num > 100:
    print("กรุณากรอกข้อมูล 0-100")