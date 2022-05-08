def validate():
    while True:
        imie = input("Podaj imię : ")
        if not imie.istitle() and not imie.isalpha():
            break
        print(imie)

        age = input("Podaj nwiek : ")
        if not age.isdecimal() and age <= 0 and age.:
            break
        print(age)

validate()

#Name
#Age
#Password
#Zip code