class DummyValidator:

    def __set_name(self, name):
        self.__name = name

    def __get_name(self):
        return self.__name

    def __set_age(self, age):
        self.__age = age

    def __get_age(self):
        return self.__age

    def __set_passwd(self, passwd):
        self.__passwd = passwd

    def __get_passwd(self):
        return self.__passwd

    def __set_zip(self, zip):
        self.__zip = zip

    def __get_zip(self):
        return self.__zip

    def __validate_name(self):
        if not self.__name.isalpha():
            return False
        return True

    def __validate_age(self):
        if not self.__age.isnumeric():
            return False
        if int(self.__age) <= 0:
            return False
        return True

    def __validate_passwd(self):
        if len(self.__passwd) == 0:
            return False
        return True

    def __validate_zip_code(self):
        if not self.__zip[0:2:].isdecimal() or not self.__zip[3:5:].isdecimal() or \
                self.__zip[2:3:] != "-" or len(self.__zip) != 6:
            return False
        return True

    def __print_validated_data(self):
        print(f"* {self.__get_name()}\n* {self.__get_age()}\n* {self.__get_passwd()}\n* {self.__get_zip()}")

    def __init__(self):
        self.__name = 'not_set'
        self.__age = 'not_set'
        self.__passwd = 'not_set'
        self.__zip = 'not_set'

    def validate_and_print(self):
        while True:
            self.__set_name(input("Podaj imię : "))
            if not self.__validate_name():
                break

            self.__set_age(input("Podaj wiek : "))
            if not self.__validate_age():
                break

            self.__set_passwd(input("Podaj hasło : "))
            if not self.__validate_passwd():
                break

            self.__set_zip(input("Podaj kod pocztowy : "))
            if not self.__validate_zip_code():
                break

            self.__print_validated_data()
