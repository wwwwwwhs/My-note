print("hello ")
height = 1.74
weight = 70.0
bmi = weight / (height * height)
if bmi<18.5:
    a = "肥胖"
elif bmi >= 18.5 and bmi < 25:
    a = "正常"
elif bmi >= 25 and bmi < 32 :
    a = "过重"
print(a)