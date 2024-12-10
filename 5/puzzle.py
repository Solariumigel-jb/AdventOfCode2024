data = {}
testData = []

with open('data.txt', 'r') as file:
    lines = file.readlines()
    isTestData = False
    for line in lines:
        line = line.replace('\r', '').replace('\n', '')

        if(not line):
            isTestData = True
            continue

        if(isTestData):
            testData.append(line.split(','))
        else:
            first, second = line.split('|')

            if(not first in data):
                data[first] = []
            data[first].append(second)

validData = []
invalidData = []
for test in testData:
    counter = 1
    isValid = True
    for element in test:
        nextElements = test[counter:]
        if(not nextElements):
            break

        if(not element in data):
            isValid = False
            break
        dic = data[element]
        k = [e for e in nextElements if e not in dic]
        if k:
            isValid = False
            break
        counter += 1
    if isValid:
        validData.append(test)
    else:
        invalidData.append(test)

result = 0
for valid in validData:
    middle = int(len(valid) / 2)
    result += int(valid[middle])
print(f"Part One: {result}")