class Employee:
    def __init__(self, salary, period, email, surname, position):
        self.__salary = salary
        self.__period = period
        self.__email = email
        self.__surname = surname
        self.__position = position

    def give_salary(self, amount):
        self.__salary += amount

    def promote(self, new_pos):
        self.__position = new_pos

    def fired(self):
        self.__period = 0

    def give_name(self):
        return self.__surname

    def give_period(self):
        return self.__period

    def give_email(self):
        return self.__email

    def give_salary(self):
        return self.__salary

    def give_position(self):
        return self.__position

    def status(self):
        print(f"{self.give_name()} : period = {self.give_period()}")




if __name__ == '__main__':

    firm = []
    employee1 = Employee(1000, 2, "employee1@op.pl", "Employee1", "dev")
    firm.append(employee1)
    employee1.status()

    employee2 = Employee(8000, 1, "employee2@op.pl", "Employee2", "tester")
    firm.append(employee2)
    employee2.status()

    employee3 = Employee(1200, 2, "employee3@op.pl", "Employee3", "sen_dev")
    firm.append(employee3)
    employee3.status()

    for i in firm:
        i.fired()

    print("After reorganization:")
    employee1.status()
    employee2.status()
    employee3.status()