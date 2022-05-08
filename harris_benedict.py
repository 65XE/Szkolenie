def harris_benedict(masa, wzrost, wiek, plec="K"):
    if plec == "M":
        return (66.47 + 13.7 * masa + 5.0 * wzrost - 6.76 * wiek)
    return (655.1 + (9.567 * masa) + (1.85 * wzrost) - (4.68 * wiek))

print(f" trzeba mu jesc {str(harris_benedict(100, 195, 30, 'M'))} kcal")
print(f" trzeba jej jesc {str(harris_benedict(100, 195, 30))} kcal")