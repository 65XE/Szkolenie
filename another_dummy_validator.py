class Person:
    def __init__(self, name='not-set', age=0, passwd='not-set', zip='not-set'):
        self.__name = name
        self.__age = age
        self.__passwd = passwd
        self.__zip = zip

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_passwd(self):
        return self.__passwd

    def get_zip(self):
        return self.__zip

class AnotherDummyValidator:
    def __init__(self):
        self.__persons = []

    def __validate_name(self, name):
        if not name.isalpha():
            return False
        return True

    def __validate_age(self, age):
        if not age.isnumeric() or int(age) <= 0:
            return False
        return True

    def __validate_passwd(self, passwd):
        if len(passwd) == 0:
            return False
        return True

    def __validate_zip_code(self, zip):
        if not zip[0:2:].isdecimal() or not zip[3:5:].isdecimal() or \
                zip[2:3:] != "-" or len(zip) != 6:
            return False
        return True

    def print_data(self):
        print("**************************")
        for p in self.__persons:
            print(f"* {p.get_name()}\n* {p.get_age()}\n* {p.get_passwd()}\n* {p.get_zip()}")
            print("**************************")

    def validate_data(self):
        while True:
            name = input("Podaj imię : ")
            if not self.__validate_name(name):
                break

            age = input("Podaj wiek : ")
            if not self.__validate_age(age):
                break

            passwd = input("Podaj hasło : ")
            if not self.__validate_passwd(passwd):
                break

            zip = input("Podaj kod pocztowy : ")
            if not self.__validate_zip_code(zip):
                break

            person = Person(name, age, passwd, zip)
            self.__persons.append(person)
            print('\n')
