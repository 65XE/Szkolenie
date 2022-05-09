from dummy_validator import DummyValidator

def validateName(name):
    if not name.isalpha():
        return False
    return True

def validateAge(age):
    if not age.isnumeric():
        return False
    if int(age) <= 0:
        return False
    return True

def validatePasswd(passwd):
    if len(passwd) == 0:
        return False
    return True

def validateZipCode(zip):
    if not zip[0:2:].isdecimal() or not zip[3:5:].isdecimal() or zip[2:3:] != "-" or len(zip) != 6:
        return False
    return True

def validate_and_print():
    while True:
        name = input("Podaj imię : ")
        if not validateName(name):
            break

        age = input("Podaj wiek : ")
        if not validateAge(age):
            break

        passwd = input("Podaj hasło : ")
        if not validatePasswd(passwd):
            break

        zip = input("Podaj kod pocztowy : ")
        if not validateZipCode(zip):
            break

        print(f"* {name}\n* {age}\n* {passwd}\n* {zip}")

if __name__ == '__main__':
    #first try
    validate_and_print()

    #second try
    validator = DummyValidator()
    validator.validate_and_print()


