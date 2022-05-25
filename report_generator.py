import csv
import json


class Report:
    def __init__(self, data):
        self.data = data


class ReportGenerator:
    def __create_dict(self, data):
        keys = ('Passed', 'Failures', 'Exceptions')
        values = (data[0], data[1], data[2])
        return dict(zip(keys, values))

    def __json_generator(self, data):
        dict = self.__create_dict(data)

        with open('report.json', 'wt', encoding='UTF8') as fout:
            json.dump(dict, fout)

    def __csv_generator(self, data):
        header = ['Passed', 'Failures', 'Exceptions']

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
                print("This is not 1 or 2. There will be no reports.")

    def generate(self, report):
        print(f"Hi,\nPlease specify in which file format you want to generate file?\n"
              f"Press 1 for JSON\nPress 2 for CSV\nPress 3 for both")
        format = input("Please enter the number : ")
        generator = self.__choose_format(format)
        return generator(report)
