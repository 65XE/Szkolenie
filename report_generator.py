from consts_and_enums import CONSTANTS
from consts_and_enums import Status
import csv
import json


# class Report:
#     def __init__(self, data):
#         self.data = data


class ReportGenerator:
    def __create_dict(self, data):
        keys = (CONSTANTS.PASSED, CONSTANTS.FAILURES, CONSTANTS.EXCEPTIONS,
                CONSTANTS.WARNINGS, CONSTANTS.SKIPPED, CONSTANTS.BLOCKED,
                CONSTANTS.WORKAROUNDS)
        values = (data[Status.PASSED], data[Status.FAILURES], data[Status.EXCEPTIONS],
                  data[Status.WARNINGS], data[Status.SKIPPED], data[Status.BLOCKED],
                  data[Status.WORKAROUNDS])
        return dict(zip(keys, values))

    def __json_generator(self, data):
        diction = self.__create_dict(data)

        with open('report.json', 'wt', encoding='UTF8') as fout:
            json.dump(diction, fout)

    def __csv_generator(self, data):
        header = [CONSTANTS.PASSED, CONSTANTS.FAILURES, CONSTANTS.EXCEPTIONS,
                  CONSTANTS.WARNINGS, CONSTANTS.SKIPPED, CONSTANTS.BLOCKED,
                  CONSTANTS.WORKAROUNDS]

        with open('report.csv', 'wt', encoding='UTF8') as fout:
            csvout = csv.writer(fout)
            csvout.writerow(header)
            csvout.writerow(data)

    def __both_generators(self, data):
        self.__json_generator(data)
        self.__csv_generator(data)

    def __choose_format(self, format):
        match format:
            case "1":
                return self.__json_generator
            case "2":
                return self.__csv_generator
            case "3":
                return self.__both_generators
            case _:
                print("This is not 1, nor 2 or even 3. There will be no reports.")
                return False

    def generate(self, report):
        print(f"Hi,\nPlease specify in which file format you want to generate file?\n"
              f"Press 1 for JSON\nPress 2 for CSV\nPress 3 for both")
        formatting = input("Please enter the number : ")
        generator = self.__choose_format(formatting)
        if generator != False:
            return generator(report)
