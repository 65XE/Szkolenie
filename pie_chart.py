import matplotlib.pyplot as plt
import numpy as np
import os
import re

def przyklad_z_czatu():
    path = "C:\\Windows"
    total_files = 0
    total_size = 0
    for dir_path, _, file_name_array in os.walk(path):
        for file_name in file_name_array:
            if not file_name.endswith(".xml"):
                continue
            total_files += 1
            full_file_path = os.path.join(dir_path, file_name)
            total_size += os.path.getsize(full_file_path)

    print(F"Liczba plików .xml to {total_files}")
    print(F"Rozmiar plików to {total_size} bajtów.")
    print(F"Rozmiar plików to {round(total_size * (10 ** -6))} megabajtów.")


def return_number_in_tags(tag, line):
        if tag in line:
            s = line
            res = s.find(">")
            s = s.replace(s[:res + 1], "")
            res = s.find("<")
            a = s.replace(s[res:], "")
            return int(a)


def exception_count(line):
    return return_number_in_tags("<Exceptions>", line)

def passed_count(line):
    return return_number_in_tags("<Passed>", line)

def failures_count(line):
    return return_number_in_tags("<Failures>", line)

def print_pie_chart(data, labels):
    plt.pie(data, labels=labels)
    plt.show()

def proba():
    path = "C:\\WORK\\prywatne\\nauka\\Szkolenie Python\\Task"

    passed = "<Passed>"
    failures = "<Failures>"
    exceptions = "<Exceptions>"
    passed_no = 0
    failures_no = 0
    exceptions_no = 0
    total_files = 0

    for dir_path, _, files in os.walk(path):
        for name in files:
            if not name.startswith("LOG_") or not name.endswith(".xml"):
                continue
            new_path = dir_path + "\\" + name
            file1 = open(new_path, "r", encoding='UTF8')
            for line in file1:
                if passed in line:
                    passed_no += passed_count(line)
                if failures in line:
                    failures_no += failures_count(line)
                if exceptions in line:
                    exceptions_no += exception_count(line)


            total_files += 1

    print(F"Liczba plików LOG*.xml które sprawdzam to:  {total_files}")
    print(f"Liczba Passów : {passed_no}")
    print(f"Liczba Faili : {failures_no}")
    print(f"Liczba Exceptionów : {exceptions_no}")

    data = np.array([passed_no, failures_no, exceptions_no])
    labels = ['Passed', 'Failures', 'Exceptions']
    print_pie_chart(data, labels)

if __name__ == '__main__':
    print(f"Poczatek")

    # y = np.array([35,25,25,15])
    #
    # plt.pie(y)
    # plt.show()

    proba()

    print(f"Koniec")