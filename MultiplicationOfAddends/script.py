import matplotlib.pyplot as plt
import numpy as np

def createPlot(count):
    def createLabels(count):
        output = []
        for num in range(count + 1):
            output.append(str(num) + ' * ' + str(count - num))
        return output

    def createNumbers(count):
        output = []
        for num in range(count + 1):
            output.append(num * (count - num))
        return output
    labels = np.array(createLabels(count))
    numbers = np.array(createNumbers(count))

    plt.bar(labels, numbers)
    plt.show()

count = int(input('Please enter your number: '))

createPlot(count)