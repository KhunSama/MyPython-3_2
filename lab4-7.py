def Circle(r):
    area = 22/7*(r**2)
    return area

r = int(input("รับค่ารัศมีวงกลม = "))
print("พื้นที่วงกลม = %d" % Circle(r))