import numpy as np

def CPU_V2(notation, a, b):
    sign_a = np.sign(a)
    octo_a = np.sign(a)*a
    octo_b = np.sign(b)*b
    if np.sign(a) * np.sign(b) == 1:
        print(sign_a*summator(notation, octo_a, octo_b))
        print(sign_a*differator(notation, octo_a, octo_b))
        print(additor(notation, octo_a, octo_b))
        print(divider(notation, octo_a, octo_b))
        return 0
    else:
        print(sign_a*differator(notation, octo_a, octo_b))
        print(sign_a*summator(notation, octo_a, octo_b))
        print(-additor(notation, octo_a, octo_b))
        print(-divider(notation, octo_a, octo_b))
        return 0

def CPU_V1(notation, a, b):
    if a >= 0 and b >= 0: 
        print(summator(notation, a, b))
        print(differator(notation, a, b))
        print(additor(notation, a, b))
        print(divider(notation, a, b))
        return 0
    if a < 0 and b < 0:
        print(-summator(notation, -a, -b))
        print(-differator(notation, -a, -b))
        print(additor(notation, -a, -b))
        print(divider(notation, -a, -b))
        return 0
    if a >= 0 and b < 0:
        print(differator(notation, a, -b))
        print(summator(notation, a, -b))
        print(-additor(notation, a, -b))
        print(-divider(notation, a, -b))
        return 0
    if a < 0 and b >= 0:
        print(-differator(notation, -a, b))
        print(-summator(notation, -a, b))
        print(-additor(notation, -a, b))
        print(-divider(notation, -a, b))
        return 0

def summator(notation, a, b):
    sum = 0
    r = 0
    i = 0
    while(True):
        numb1 = a % (10**(i+1)) // (10**i)
        numb2 = b % (10**(i+1)) // (10**i)
        if numb1 + numb2 + r >= notation:
            sum += (numb1 + numb2 - notation + r)*(10**i)
            r = 1
        else:
            sum += (numb1 + numb2 + r)*(10**i)
            r = 0
        if a < 10**(i+1) and b < 10**(i+1) and r == 0:
            break
        i+=1
    return sum

def differator(notation, a, b):
    if a >= b:
        i = a
        while(True):
            if summator(notation, i, b) == a:
                return i
            i -= 1
    if a < b:
        i = b
        while(True):
            if summator(notation, i, a) == b:
                return -i
            i-=1

def additor(notation, a, b):
    sum = 0
    add = 0
    r = 0
    i = 0
    j = 0
    while(b >= 10**i or r != 0):
        numb2 = b % (10**(i+1)) // (10**i)
        while(a >= 10**j or r != 0):
            numb1 = a % (10**(j+1)) // (10**j)
            sumN1N2_R = summator(notation, numb1*numb2, r)
            s = sumN1N2_R % notation
            r = sumN1N2_R // notation
            sum += s * 10**j
            j += 1
        add = summator(notation, add, sum*10**i)
        j = 0
        sum = 0
        i += 1
    return add

def divider(notation, a, b):
    c = 1
    while(additor(notation, c, b) <= a):
        if additor(notation, c, b) == a:
            return c
        c = summator(notation, c, 1)
    return "Не делится нацело"

notation = int(input("Введите систему счисления: "))
a, b  = map(int, input("Введите 2 числа: ").split())
CPU_V2(notation, a, b)