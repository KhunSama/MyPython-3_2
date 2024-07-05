def Fahrenheit(C):
    temp = ((9/5)*C) +32
    return temp

def Kelvin(C):
    temp = C + 273.15
    return temp

C = float(input("อุณหภูมิเซลเซียส = "))
print("อุณหภูมิฟาเรนไฮส์ = %.2f" % Fahrenheit(C))
print("อุณหภูมิเคลวิน = %.2f" % Kelvin(C))