import re

regex = r'mul\([0-9]{1,3}\,[0-9]{1,3}\)|don\'t\(\)|do\(\)'
p = re.compile(regex)

result = 0
isEnabled = True
with open('data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        foundElements = p.findall(line)
        for element in foundElements:
            if(element == 'do()'):
                isEnabled = True
            elif(element == "don't()"):
                isEnabled = False
            elif(isEnabled):
                values = element.replace('mul(', '').replace(')', '').split(',')
                result += int(values[0]) * int(values[1])

print(f'result: {result}')