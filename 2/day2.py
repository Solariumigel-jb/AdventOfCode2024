import numpy as np

def validateRow(array):
    isSave = True
    isIncreasing = (array[0] - array[1]) > 0

    lastValue = array[0]
    for x in range(1, len(array)):
        if(not isSave):
            return False
        currentValue = array[x]
        different = lastValue - currentValue
        if(isIncreasing):
            isSave = different in [1, 2, 3]
        else:
            isSave = different in [-1, -2, -3]

        lastValue = currentValue

    return isSave

fullarray = list()
with open('data.tsv', "r") as file:
    for line in file:
        array = np.fromstring(line, dtype=int, sep=' ')
        fullarray.append(array)

areSave = 0
for x in fullarray:
    isSave = validateRow(x)
    if(isSave):
        areSave += 1
print(areSave)