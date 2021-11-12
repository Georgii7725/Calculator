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
    c = a
    while(additor(notation, c, b)>=a):
        if additor(notation, c, b) == a:
            return c
        c = differator(notation, c, 1)
    return "Не делится нацело"

notation = int(input("Введите систему счисления: "))
a, b = map(int, input("Введите 2 числа: ").split())
op = input("Введите операцию над ними: ")

if op == "+":
    print(summator(notation, a, b))
elif op == "-": 
    print(differator(notation, a, b))
elif op == "*":
    print(additor(notation, a, b))
elif op == "/":
    print(divider(notation, a, b))
else:
    print("Error")