import numpy as np

def validateForPartTwo(array):

    if validateForPartOne(array):
        return True

    for x in range(len(array)):
        if validateForPartOne(np.delete(array, x, 0)):
            return True
    return False

def validateForPartOne(array):
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

areSavePart1 = 0
areSavePart2 = 0
for x in fullarray:
    if validateForPartOne(x):
        areSavePart1 += 1

    if validateForPartTwo(x):
        areSavePart2 += 1

print(f'Part One: {areSavePart1}')
print(f'Part Two: {areSavePart2}')