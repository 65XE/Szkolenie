from tests_counter import TestsCounter
from charts_generator import ChartGenerator

if __name__ == '__main__':
    tests_counter = TestsCounter(r"D:\development\Projects\Python\Task")#os.path.join
    tests_counter.run()
    tests_counter.print_summary()

    chart = ChartGenerator()
    labels = ['Passed', 'Failures', 'Exceptions']
    chart.print_pie_chart(tests_counter.get_data_for_chart(), labels, "Wyniki Testów")
