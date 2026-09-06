"""
This is a program that converts binary or decimal into decimal, octal, or hex.

Team Members: 
- Melissa Castaneda
- David
- Frank
"""


class main:
    # this saves the input and the type of conversion it is
    def __init__(self, num, conversion):
        self.num = num
        self.conversion = conversion

    # this checks through to see that each character is a number and contains
    # only one period
    # strInput would be the user input, if it fails the test then it returns False
    # conversionType takes the type of conversion to check for their rules
    @staticmethod
    def inputValChecker(numValStr, conversionType) -> bool:
        dotChecker = 0
        for c in numValStr:
            if c == '.':
                if dotChecker > 0:
                    return False
                else:
                    dotChecker += 1
            elif conversionType == 'Decimal':
                if not c.isdigit():
                    return False
            elif conversionType == 'Binary':
                if c != '0' and c != '1':
                    return False
        return True


# this ask the user to input what they want to convert from
userInput = input('Which of the following would you like to convert from\n'
                  'Type 1 or 2\n'
                  '1. Decimal\n'
                  '2. Binary\n')

# this checks that the user only chooses between those two options or else it loops
while userInput != '1' and userInput != '2':
    userInput = input('Which of the following would you like to convert from\n'
                      'Type 1 or 2\n'
                      '1. Decimal\n'
                      '2. Binary\n')

# overwrites the variable into the type they are converting form
if userInput == '1':
    userInput = 'Decimal'
else:
    userInput = 'Binary'

# check the input value is correct format by passing through the method inputValChecker
numValStr = str(input('What is the number you\'d like? \n'))
while main.inputValChecker(numValStr, userInput) == False:
    numValStr = str(
        input('This is an incorrect value \nWhat is the number you\'d like? \n'))

# saves the inputs, ready for conversion
preset = main(num=numValStr, conversion=userInput)

"""
Decimal conversion code below.
"""

# turns one decimal character into a number
def digitValue(c):
    digits = '0123456789'

    for i in range(10):
        if c == digits[i]:
            return i


# turns a decimal string into a whole number
def decimalWhole(numStr):
    number = 0

    for c in numStr:
        number = number * 10 + digitValue(c)

    return number


# converts the whole number using division
def convertWhole(numStr, base):
    digits = '0123456789ABCDEF'

    if numStr == '':
        return '0'

    number = decimalWhole(numStr)

    if number == 0:
        return '0'

    answer = ''

    while number > 0:
        remainder = number % base
        answer = digits[remainder] + answer
        number = number // base

    return answer


# converts the decimal fraction using multiplication
def convertFraction(numStr, base, places):
    digits = '0123456789ABCDEF'

    numerator = 0
    denominator = 1

    # makes the decimal into a fraction
    for c in numStr:
        numerator = numerator * 10 + digitValue(c)
        denominator = denominator * 10

    answer = ''

    # multiplication method
    for i in range(places):
        numerator = numerator * base

        digit = numerator // denominator
        numerator = numerator % denominator

        answer += digits[digit]

    return answer


# converts decimal to another base
def decimalToBase(numStr, base, places):
    wholePart = ''
    fractionPart = ''
    foundDot = False

    # separates whole and fraction
    for c in numStr:

        if c == '.':
            foundDot = True

        elif foundDot == False:
            wholePart += c

        else:
            fractionPart += c

    wholeAnswer = convertWhole(wholePart, base)

    fractionAnswer = convertFraction(
        fractionPart,
        base,
        places
    )

    return wholeAnswer + '.' + fractionAnswer


# only runs this part for decimal input
if preset.conversion == 'Decimal':

    # 16 binary digits after point
    binaryAnswer = decimalToBase(
        preset.num,
        2,
        16
    )

    # 6 octal digits after point
    octalAnswer = decimalToBase(
        preset.num,
        8,
        6
    )

    # 4 hexadecimal digits after point
    hexAnswer = decimalToBase(
        preset.num,
        16,
        4
    )

    print('\nDecimal:', preset.num)
    print('Binary:', binaryAnswer)
    print('Octal:', octalAnswer)
    print('Hexadecimal:', hexAnswer)
