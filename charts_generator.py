import matplotlib.pyplot as plt

class ChartGenerator:
    def __init(self, data=[], labels=[], title=""):
        self.__data = data
        self.__labels = labels
        self.__title = title

    def print_pie_chart(self, data, labels, title):
        fig, ax = plt.subplots(figsize=(6, 6))
        pie_colors = ['tab:green', 'tab:orange', 'tab:red']
        ax.pie(data, labels=labels, colors=pie_colors, autopct='%.1f%%',
               wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
               textprops={'size': 'x-large'})
        ax.set_title(title, fontsize=18)
        label = [f"Passed : {data[0]}", f"Failures : {data[1]}", f"Exceptions : {data[2]}"]
        plt.legend(labels=label, loc='upper center',
                   bbox_to_anchor=(0.5, -0.04), ncol=2)
        plt.tight_layout()
        plt.show()