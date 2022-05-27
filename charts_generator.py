import matplotlib.pyplot as plt
from consts_and_enums import Status
from consts_and_enums import CONSTANTS


class ChartGenerator:
    def __init(self, data=[], labels=[], title=""):
        self.__data = data
        self.__labels = labels
        self.__title = title

    @staticmethod
    def __check_if_small(data, labels):
        all = 0
        ctr = 0
        for i in data:
            all += i
        for i in data:
            if i <= 100 * float(i)/float(all):
                labels[ctr] = ''
            ctr += 1

    def print_pie_chart(self, data, labels, title):
        self.__check_if_small(data, labels)
        fig, ax = plt.subplots(figsize=(8, 6))
        pie_colors = ['tab:green', 'tab:orange', 'tab:red', 'tab:olive', 'tab:grey',
                      'tab:purple', 'tab:cyan']
        explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
        ax.pie(data, explode=explode, colors=pie_colors, labels=labels,
               autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '',
               wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
               textprops={'size': 'x-large'}, shadow=True)
        ax.set_title(title, fontsize=18, fontweight='bold')
        label = [f"{CONSTANTS.PASSED} : {data[Status.PASSED]}",
                 f"{CONSTANTS.FAILURES} : {data[Status.FAILURES]}",
                 f"{CONSTANTS.EXCEPTIONS} : {data[Status.EXCEPTIONS]}",
                 f"{CONSTANTS.WARNINGS} : {data[Status.WARNINGS]}",
                 f"{CONSTANTS.SKIPPED} : {data[Status.SKIPPED]}",
                 f"{CONSTANTS.BLOCKED} : {data[Status.BLOCKED]}",
                 f"{CONSTANTS.WORKAROUNDS} : {data[Status.WORKAROUNDS]}"]
        plt.legend(labels=label, loc='center',
                   bbox_to_anchor=(0.5, -0.04), ncol=4)
        plt.tight_layout()
        plt.show()
