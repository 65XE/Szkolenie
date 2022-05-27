from consts_and_enums import CONSTANTS
from consts_and_enums import Status
import numpy as np
import os


class TestsCounter:
    def __init__(self, path):
        self.__path = path
        self.__data = []

    @staticmethod
    def __return_number_in_tags(tag, line):
        if tag in line:
            s = line
            res = s.find(">")
            s = s.replace(s[:res + 1], "")
            res = s.find("<")
            a = s.replace(s[res:], "")
            return int(a)

    def __exception_count(self, line):
        return self.__return_number_in_tags(CONSTANTS.EXCEPTIONS_TAG, line)

    def __passed_count(self, line):
        return self.__return_number_in_tags(CONSTANTS.PASSED_TAG, line)

    def __failures_count(self, line):
        return self.__return_number_in_tags(CONSTANTS.FAILURES_TAG, line)

    def __warnings_count(self, line):
        return self.__return_number_in_tags(CONSTANTS.WARNINGS_TAG, line)

    def __skipped_count(self, line):
        return self.__return_number_in_tags(CONSTANTS.SKIPPED_TAG, line)

    def __blocked_count(self, line):
        return self.__return_number_in_tags(CONSTANTS.BLOCKED_TAG, line)

    def __workarounds_count(self, line):
        return self.__return_number_in_tags(CONSTANTS.WORKAROUNDS_TAG, line)

    def __get_passed(self):
        return self.__data[Status.PASSED]

    def __get_failures(self):
        return self.__data[Status.FAILURES]

    def __get_exceptions(self):
        return self.__data[Status.EXCEPTIONS]

    def __get_warnings(self):
        return self.__data[Status.WARNINGS]

    def __get_skipped(self):
        return self.__data[Status.SKIPPED]

    def __get_blocked(self):
        return self.__data[Status.BLOCKED]

    def __get_workarounds(self):
        return self.__data[Status.WORKAROUNDS]

    def __get_total_files(self):
        return self.__data[Status.TOTAL_FILES]

    def __set_data(self, data):
        for i in data:
            self.__data.append(i)

    def run(self):
        passed_no = 0
        failures_no = 0
        exceptions_no = 0
        warnings_no = 0
        skipped_no = 0
        blocked_no = 0
        workarounds_no = 0
        total_files = 0
        for dir_path, _, files in os.walk(self.__path):
            for name in files:
                if not name.startswith("LOG_") or not name.endswith(".xml"):
                    continue
                new_path = dir_path + "\\" + name
                file = open(new_path, "r", encoding='UTF8')
                for line in file:
                    if CONSTANTS.PASSED_TAG in line:
                        passed_no += self.__passed_count(line)
                    if CONSTANTS.FAILURES_TAG in line:
                        failures_no += self.__failures_count(line)
                    if CONSTANTS.EXCEPTIONS_TAG in line:
                        exceptions_no += self.__exception_count(line)
                    if CONSTANTS.WARNINGS_TAG in line:
                        warnings_no += self.__warnings_count(line)
                    if CONSTANTS.SKIPPED_TAG in line:
                        skipped_no += self.__skipped_count(line)
                    if CONSTANTS.BLOCKED_TAG in line:
                        blocked_no += self.__blocked_count(line)
                    if CONSTANTS.WORKAROUNDS_TAG in line:
                        workarounds_no += self.__workarounds_count(line)

                total_files += 1
        self.__set_data([passed_no, failures_no, exceptions_no, warnings_no,
                        skipped_no, blocked_no, workarounds_no, total_files])

    def print_summary(self):
        print(f"Liczba plików LOG*.xml które sprawdzam to:  {self.__get_total_files()}")
        print(f"Liczba Passów : {self.__get_passed()}")
        print(f"Liczba Faili : {self.__get_failures()}")
        print(f"Liczba Exceptionów : {self.__get_exceptions()}")
        print(f"Liczba Warningów : {self.__get_warnings()}")
        print(f"Liczba Skipped : {self.__get_skipped()}")
        print(f"Liczba Blocked : {self.__get_blocked()}")
        print(f"Liczba Workarounds : {self.__get_workarounds()}")

    def get_data_for_chart(self):
        return np.array(self.get_data())

    def get_data(self):
        return [self.__get_passed(), self.__get_failures(), self.__get_exceptions(),
                self.__get_warnings(), self.__get_skipped(), self.__get_blocked(),
                self.__get_workarounds()]
