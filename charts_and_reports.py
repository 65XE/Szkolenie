from tests_counter import TestsCounter
from report_generator import ReportGenerator
from charts_generator import ChartGenerator
from consts_and_enums import CONSTANTS

if __name__ == '__main__':
    # tests counting
    tests_counter = TestsCounter(r"D:\development\Projects\Python\Task")#os.path.join
    tests_counter.run()
    tests_counter.print_summary()

    #generate chart
    chart = ChartGenerator()
    labels = [CONSTANTS.PASSED, CONSTANTS.FAILURES, CONSTANTS.EXCEPTIONS,
              CONSTANTS.WARNINGS, CONSTANTS.SKIPPED, CONSTANTS.BLOCKED,
              CONSTANTS.WORKAROUNDS]
    chart.print_pie_chart(tests_counter.get_data_for_chart(), labels, "Wyniki Testów")

    # generate report
    report = tests_counter.get_data()
    report_generator = ReportGenerator()
    report_generator.generate(report)
