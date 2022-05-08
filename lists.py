def arytmetyczna(x):
    res = 0
    for i in x:
        res += i
    print(str(res / len(x)))

def harmoniczna(x):
    res = 0
    for i in x:
        res += 1/i
    print(str(len(x)/res))

def geometryczna(x):
    res = 1
    for i in x:
        res *= i
    print(str(res ** (1/len(x))))

#z = [1,2,3]
x = [1,2,3,4,5,6,7,8,9]
arytmetyczna(x)
harmoniczna(x)
geometryczna(x)


#jaka jest srednia arytmetyczna, harmoniczna, geometryczna