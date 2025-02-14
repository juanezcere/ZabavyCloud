"""
Plot utils.
"""
import matplotlib.pyplot as plt


@staticmethod
def show(values: dict, title: str = 'Gráfico', xlabel: str = 'Time', ylabel: str = 'Value') -> None:
    plt.plot(values['timestamp'], values['battery'], color='g')
    plt.plot(values['timestamp'], values['temperature'], color='r')
    plt.plot(values['timestamp'], values['humidity'], color='b')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

