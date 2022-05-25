import csv
import json

class ReportGenerator:
    def __init__(self, data):
        self.__data = data

    def __create_dict(self):
        keys = ('Passed', 'Failures', 'Exceptions')
        values = (self.__data[0], self.__data[1], self.__data[2])
        return dict(zip(keys, values))

    def __json_generator(self):
        data = self.__create_dict()

        with open('report.json', 'wt', encoding='UTF8') as fout:
            json.dump(data, fout)


    def __csv_generator(self):
        header = ['Passed', 'Failures', 'Exceptions']

        with open('report.csv', 'wt', encoding='UTF8') as fout:
            csvout = csv.writer(fout)
            csvout.writerow(header)
            csvout.writerow(self.__data)

    def __choose_format(self, format):
        match format:
            case "1":
                self.__json_generator()
            case "2":
                self.__csv_generator()
            case "3":
                self.__json_generator()
                self.__csv_generator()
            case _:
                print("This is not 1 or 2. There will be no reports.")

    def generate(self):
        print(f"Hi,\nPlease specify in which file format you want to generate file?\n"
              f"Press 1 for JSON\nPress 2 for CSV\nPress 3 for both")
        format = input("Please enter the number : ")
        self.__choose_format(format)