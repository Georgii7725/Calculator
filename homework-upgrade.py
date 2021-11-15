def sum_mass(a):
    ans = 0
    for i in a:
        ans += i
    return ans

def join(a): # Uns -> Uns
    numb = 0
    for i in range(1, len(a)+1):
        numb += a[-i]*10**(i-1)
        i += 1
    return numb

def getKey(value):
    for k, v in dict.items():
        if v == value:
            return k

def transNumber(a): 
    ans = ""
    for i in range(1, len(a[1:]) + 1):
        ans = str(getKey(a[-i])) + ans
    if a[0] == 1:
        return ans
    else:
        return "-" + ans

def dekrement(notation, a):
    if a[-1] == 0:
        a = dekrement(notation, a[:-1]) + [notation-1]
        if a[0] == 0:
            return a[1:]
        return a
    a[-1] -= 1
    return a

def CPU_V2(notation, a, b):
    if a[0] * b[0] == 1:
        print(transNumber([a[0]] + summator(notation, a[1:], b[1:])))
        d = differator(notation, a[1:], b[1:])
        print(transNumber([a[0]*d[0]] + d[1:]))
        print(transNumber([1] + additor(notation, a[1:], b[1:])))
        d = divider(notation, a[1:], b[1:])
        if d == "Не делится нацело":
            print(d)
        else:
            print(transNumber([1] + d))
        return 0
    else:
        d = differator(notation, a[1:], b[1:])
        print(transNumber([a[0]*d[0]] + d[1:]))
        print(transNumber([a[0]] + summator(notation, a[1:], b[1:])))
        print(transNumber([-1] + additor(notation, a[1:], b[1:])))
        print(transNumber([-1] + divider(notation, a[1:], b[1:])))
        return 0

def summator(notation, a, b): # Uns -> Uns
    MAX = max(len(a), len(b))
    if MAX == len(a):
        a = [0] + a
        b = [0]*(MAX-len(b) + 1) + b
    else:
        a = [0]*(MAX-len(a) + 1) + a
        b = [0] + b
    sum = [0]*(MAX+1)
    r = 0
    i = 1
    while(True):
        if a[-i] + b[-i] + r >= notation:
            sum[-i] = a[-i] + b[-i] + r - notation
            r = 1
        else:
            sum[-i] += a[-i] + b[-i] + r
            r = 0
        if i >= len(a) and i >= len(b) and r == 0:
            break
        i+=1
    if sum[0] == 0:
        return sum[1:]
    else:
        return sum

def differator(notation, a, b): #Uns -> Sign
    if join(a) >= join(b):
        c = a.copy()
        while(True):
            if summator(notation, c, b) == a:
                return [1] + c
            c = dekrement(notation, c)
    if join(a) < join(b):
        c = b
        while(True):
            if summator(notation, c, a) == b:
                return [-1] + c
            c = dekrement(notation, c)

def additor(notation, a, b): #Uns -> Uns
    Len_a = len(a)
    Len_b = len(b)
    if max(Len_a, Len_b) == Len_a:
        b = [0] * (Len_a - Len_b + 1) + b
        a = [0] + a
    else:
        a = [0] * (Len_b - Len_a + 1) + a
        b = [0] + b
    add = [0] * (Len_a + Len_b)
    i = 1
    while(i <= Len_b or r != 0):
        r = 0
        j = 1
        sum = [0] * (Len_a + Len_b)
        while(j <= Len_a  or r != 0):
            sumN1N2_R = a[-j]*b[-i] + r
            s = sumN1N2_R % notation
            r = sumN1N2_R // notation
            sum[-j] += s
            j += 1
        while(True):
            if sum_mass(sum) == 0:
                break
            if sum[0] == 0:
                sum = sum[1:]
            else:
                break
        add = summator(notation, add, sum + [0]*(i-1))
        i += 1
    while(True):
        if add[0] == 0:
            add = add[1:]
        else: break   
    return add

def divider(notation, a, b): #Uns -> Uns
    c = a.copy()
    while(differator(notation, additor(notation, c, b), a)[0] == 1):
        if additor(notation, c, b) == a:
            return c
        c = dekrement(notation, c)
    return "Не делится нацело"

dict = {"0" : 0,
        "1" : 1,
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
        "A" : 10,
        "B" : 11,
        "C" : 12,
        "D" : 13,
        "E" : 14, 
        "F" : 15, 
        "G" : 16, 
        "H" : 17, 
        "I" : 18, 
        "J" : 19, 
        "K" : 20, 
        "L" : 21, 
        "M" : 22, 
        "N" : 23, 
        "O" : 24, 
        "P" : 25, 
        "Q" : 26, 
        "R" : 27, 
        "S" : 28, 
        "T" : 29, 
        "U" : 30, 
        "V" : 31, 
        "W" : 32, 
        "X" : 33, 
        "Y" : 34, 
        "Z" : 35 
        }

notation = int(input("Введите систему счисления: "))
a, b  = map(list, input("Введите 2 числа: ").split())
if a[0] == "-":
    a[0] = -1
else:
    a = [1] + a
if b[0] == "-":
    b[0] = -1
else:
    b = [1] + b
for i in range(1, len(a)):
    a[i] = dict[a[i]]
for i in range(1, len(b)):
    b[i] = dict[b[i]]
CPU_V2(notation, a, b)