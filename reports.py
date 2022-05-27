from report_generator import ReportGenerator
from tests_counter import TestsCounter

if __name__ == '__main__':
    #tests counting
    tests_counter = TestsCounter(r"D:\development\Projects\Python\Task")#os.path.join
    tests_counter.run()
    tests_counter.print_summary()

    #generate report
    report = tests_counter.get_data()
    report_generator = ReportGenerator()
    report_generator.generate(report)
