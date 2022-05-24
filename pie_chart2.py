import matplotlib.pyplot as plt
import numpy as np
import os


class ChartGenerator:
    def __init(self, data=[], labels=[], title=""):
        self.__data = data
        self.__labels = labels
        self.__title = title

    def print_pie_chart(self, data, labels, title):
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(data, labels=labels, autopct='%.1f%%',
               wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
               textprops={'size': 'x-large'})
        ax.set_title(title, fontsize=18)
        plt.tight_layout()
        plt.show()


class TestsCounter:
    class DataContainer:
        def __init__(self, passed_no=0, failures_no=0, except_no=0, total_files=0):
            self.__passed_no = passed_no
            self.__failures_no = failures_no
            self.__exceptions_no = except_no
            self.__total_files = total_files

        def get_passed(self):
            return self.__passed_no

        def get_failures(self):
            return self.__failures_no

        def get_exceptions(self):
            return self.__exceptions_no

        def get_total_files(self):
            return self.__total_files

        def set_data(self, passed, failures, excep, t_files):
            self.__passed_no = passed
            self.__failures_no = failures
            self.__exceptions_no = excep
            self.__total_files = t_files

    def __init__(self, path):
        self.__path = path
        self.__passed = "<Passed>"
        self.__failures = "<Failures>"
        self.__exceptions = "<Exceptions>"
        self.__data = self.DataContainer()

    def __return_number_in_tags(self, tag, line):
        if tag in line:
            s = line
            res = s.find(">")
            s = s.replace(s[:res + 1], "")
            res = s.find("<")
            a = s.replace(s[res:], "")
            return int(a)

    def __exception_count(self, line):
        return self.__return_number_in_tags("<Exceptions>", line)

    def __passed_count(self, line):
        return self.__return_number_in_tags("<Passed>", line)

    def __failures_count(self, line):
        return self.__return_number_in_tags("<Failures>", line)

    def run(self):
        passed_no = 0
        failures_no = 0
        exceptions_no = 0
        total_files = 0
        for dir_path, _, files in os.walk(self.__path):
            for name in files:
                if not name.startswith("LOG_") or not name.endswith(".xml"):
                    continue
                new_path = dir_path + "\\" + name
                file = open(new_path, "r", encoding='UTF8')
                for line in file:
                    if self.__passed in line:
                        passed_no += self.__passed_count(line)
                    if self.__failures in line:
                        failures_no += self.__failures_count(line)
                    if self.__exceptions in line:
                        exceptions_no += self.__exception_count(line)
                total_files += 1
        self.__data.set_data(passed_no, failures_no, exceptions_no, total_files)

    def print_summary(self):
        print(f"Liczba plików LOG*.xml które sprawdzam to:  {self.__data.get_total_files()}")
        print(f"Liczba Passów : {self.__data.get_passed()}")
        print(f"Liczba Faili : {self.__data.get_failures()}")
        print(f"Liczba Exceptionów : {self.__data.get_exceptions()}")

    def get_data(self):
        return np.array([self.__data.get_passed(), self.__data.get_failures(), self.__data.get_exceptions()])


if __name__ == '__main__':
    print(f"Poczatek")

    tests_counter = TestsCounter("D:\development\Projects\Python\Task")
    tests_counter.run()
    tests_counter.print_summary()

    chart = ChartGenerator()
    labels = ['Passed', 'Failures', 'Exceptions']
    chart.print_pie_chart(tests_counter.get_data(), labels, "Wyniki Testów")
