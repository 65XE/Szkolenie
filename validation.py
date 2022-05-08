def debug():
    x = "54-117"
    y = x[2:3:]

    if x[2:3:] != '-':
        print(f"To NIE jest -> {x[2:3:]} <-")
    if x[2:3:] == '-':
        print(f"To jest -> {x[2:3:]} <-")

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
    if not (zip[0:2:].isdecimal() and zip[3:5:].isdecimal()) and zip[2:3:] != '-' and len(zip) != 6:
        return False
    return True

def validate():
    name = ''
    age = ''
    passwd = ''
    zip = ''
    while True:
        # name = input("Podaj imię : ")
        # if not validateName(name):
        #     break
        #
        # age = input("Podaj wiek : ")
        # if not validateAge(age):
        #     break
        #
        # passwd = input("Podaj hasło : ")
        # if not validatePasswd(passwd):
        #     break

        zip = input("Podaj kod pocztowy : ")
        if not validateZipCode(zip):
            break

        print(f"* {name}\n* {age}\n* {passwd}\n* {zip}")

debug()
validate()

# Name
# Age
# Password
# Zip code
