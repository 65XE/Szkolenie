def bmi(masa, wzrost):
    wynik = masa / wzrost ** 2

    if (18.5 < wynik < 25):
        return "Porzadana masa ciala"
    elif wynik < 18.5:
        return "Niedowaga"
    elif (25 <= wynik < 30):
        return "Nadwaga"
    else:
        return "Otyłość"

masa = float(input("Podaj mase ciala[kg] : "))
wzrost = float(input("Podaj wzrost[m] : "))
ble = bmi(masa, wzrost)
print(ble)
