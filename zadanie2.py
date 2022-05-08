def is_palindrom(x):
    return x == x[::-1]

x = input("Podaj potencjalny palindrom : ")
print(is_palindrom(x))