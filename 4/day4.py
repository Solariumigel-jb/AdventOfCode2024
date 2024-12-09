def findPart1(lineCounter, letterCounter, array, lineStep, letterStep):
    t = 3 * lineStep
    x = 3 * letterStep
    if len(array) <= (lineCounter + t) or (lineCounter + t) < 0:
        return False
    if len(array[lineCounter]) <= (letterCounter + x) or (letterCounter + x) < 0:
        return False
    if not array[lineCounter + (1 * lineStep)][letterCounter + (1 * letterStep)] == 'M':
        return False
    if not array[lineCounter + (2 * lineStep)][letterCounter + (2 * letterStep)] == 'A':
        return False
    if not array[lineCounter + (3 * lineStep)][letterCounter + (3 * letterStep)] == 'S':
        return False

    return True

def findPart2(lineCounter, letterCounter, array):
    if lineCounter == 0 or letterCounter == 0:
        return False
    if len(array) == (lineCounter + 1) or len(array[lineCounter]) == (letterCounter + 1):
        return False
    d = str(array[lineCounter - 1][letterCounter - 1]) + "A" + str(array[lineCounter + 1][letterCounter + 1])
    t = str(array[lineCounter + 1][letterCounter - 1]) + "A" + str(array[lineCounter - 1][letterCounter + 1])

    return (d == "MAS" or d[::-1] == "MAS") and (t == "MAS" or t[::-1] == "MAS")

array = list()
with open('data.txt', "r") as file:

    lines = file.readlines()
    for x in lines:
        line = x.replace('\n', '').replace('\r', '').upper()
        array.append(line)

foundCounterPart1 = 0
foundCounterPart2 = 0
lineCounter = 0
for line in array:
    letterCounter = 0
    for letter in line:
        if(letter == 'X'):
            if findPart1(lineCounter, letterCounter, array, 0, 1):
                foundCounterPart1 += 1
            if findPart1(lineCounter, letterCounter, array, 0, -1):
                foundCounterPart1 += 1
            if findPart1(lineCounter, letterCounter, array, 1, -1):
                foundCounterPart1 += 1
            if findPart1(lineCounter, letterCounter, array, 1, 0):
                foundCounterPart1 += 1
            if findPart1(lineCounter, letterCounter, array, 1, 1):
                foundCounterPart1 += 1
            if findPart1(lineCounter, letterCounter, array, -1, -1):
                foundCounterPart1 += 1
            if findPart1(lineCounter, letterCounter, array, -1, 0):
                foundCounterPart1 += 1
            if findPart1(lineCounter, letterCounter, array, -1, 1):
                foundCounterPart1 += 1

        if letter == 'A':
            if findPart2(lineCounter, letterCounter, array):
                foundCounterPart2 += 1

        letterCounter += 1
    lineCounter += 1

print(f'Part One: {foundCounterPart1}')
print(f'Part Two: {foundCounterPart2}')