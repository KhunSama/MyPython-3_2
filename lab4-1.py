#ชนิดข้อมูลแบบ List
person = ["Chatchapol", 17, 172, 52.2, "6529011037@cdti.ac.th"]
print(person)
person[1] = 40
print("อายุ %d " % person[1])
print("ส่วนสูง %d น้ำหนัก %d " % (person[2], person[3]))
print("อีเมล %s " % person[4])

print(person[0:3])
print(person[2:4])
print(person[2:])
print(person[0:4])
print(person[-4:-1])