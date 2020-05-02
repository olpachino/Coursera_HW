y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())
kl = x1 - 2
kr = x1 + 2
if y2 <= y1:
    print('NO')
elif ((y1 % 2 != 0) and (x1 % 2 != 0)) or ((y1 % 2 == 0) and (x1 % 2 == 0)):
    if ((y2 % 2 != 0) and (x2 % 2 != 0)) or ((y2 % 2 == 0) and (x2 % 2 == 0)):
        if (x2 < kl) and (y2 < kl + y1):
            print('NO')
        elif (x2 > kr) and (y2 <= 8 - kr + y1):
            print('NO')
        else:
            print('YES')
    else:
        print('NO')
elif ((y1 % 2 != 0) and (x1 % 2 == 0)) or ((y1 % 2 == 0) and (x1 % 2 != 0)):
    if ((y2 % 2 != 0) and (x2 % 2 == 0)) or ((y2 % 2 == 0) and (x2 % 2 != 0)):
        if (x2 < kl) and (y2 < kl + y1):
            print('NO')
        elif (x2 > kr) and (y2 <= 8 - kr + y1):
            print('NO')
        else:
            print('YES')
    else:
        print('NO')
