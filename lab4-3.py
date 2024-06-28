x = {
     "name": "ชัชพล",
     "age":17,
     "wt":52,
     "h":172
     }

print(x)
print("สวัสดีครับคุณ %s " % x["name"])
print("พ.ศ.เกิด %d อายุ %d" % (2567-x["age"], x["age"]))
print("น้ำหนัก %d ส่วนสูง %d" % (x["wt"], x["h"]))