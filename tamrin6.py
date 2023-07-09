a=float(input("vazn khod ra vared kond(kg): "))
b=float(input("ghaad khod ra vared konid(m): "))
bma=a/(b**2)*10000
print("BMI shoma :",bma)
if bma>=40:
    print("shoma azafe vazn darage 4 darid!")
elif 35<=bma<=39.9:
    print("shoma azafe vazn darage 3 darid!")
elif 30<=bma<=34.9:
    print("shoma azafe vazn darage 2 darid!")
elif 25<=bma<=29.9:
    print("shoma azafe vazn darid darid!")
elif 18.5<=bma<=24.9:
    print("shoma normal hastid!")
elif bma<=18.5:
    print("kam bod vazn darid!")
elif bma<=16.5:
    print("kambod vazn darage 2 darid!")
else:
    print('kambod vazn khili shadid!')