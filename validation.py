
from dummy_validator import DummyValidator
from another_dummy_validator import AnotherDummyValidator


def validate_name(name):
    if not name.isalpha():
        return False
    return True


def validate_age(age):
    if not age.isnumeric():
        return False
    if int(age) <= 0:
        return False
    return True


def validate_passwd(passwd):
    if len(passwd) == 0:
        return False
    return True


def validate_zip_code(zip):
    if not zip[0:2:].isdecimal() or not zip[3:5:].isdecimal() or zip[2:3:] != "-" or len(zip) != 6:
        return False
    return True


def validate_and_print():
    while True:
        name = input("Podaj imię : ")
        if not validate_name(name):
            break

        age = input("Podaj wiek : ")
        if not validate_age(age):
            break

        passwd = input("Podaj hasło : ")
        if not validate_passwd(passwd):
            break

        zip = input("Podaj kod pocztowy : ")
        if not validate_zip_code(zip):
            break

        print(f"* {name}\n* {age}\n* {passwd}\n* {zip}")


if __name__ == '__main__':

    print('Którą wersję chcesz uruchomić? [1:3]\n\t1 : Funkcje.\n\t2 : Klasa DummyValidator.'
          '\n\t3 : Klasa Validatora + Person')
    x = input("Podaj cyfrę : ")
    while x == '1' or x == '2' or x == '3':
        print("==============WLAZL==================")
        # x = input("Podaj cyfrę : ")
        if x == '1':
            # first try with functions
            validate_and_print()
        elif x == '2':
            # second try with class object
            validator = DummyValidator()
            validator.validate_and_print()
        elif x == '3':
            # third try with two classes
            next_validator = AnotherDummyValidator()
            next_validator.validate_data()
            next_validator.print_data()
        else:
            print(f" {x} to nie jest cyfra z przedzialu [ 1:3 ].")
        x = input("Wybierz cyfre [1 : 3] albo wciśnij cokolwiek innego w celu zamknięcia programu : ")

