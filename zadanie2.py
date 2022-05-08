def is_palindrom(x):
    return x == x[::-1]

x = input("Podaj potencjalny palindrom : ")

#x == x[::-1]

z = is_palindrom(x)
print(z)