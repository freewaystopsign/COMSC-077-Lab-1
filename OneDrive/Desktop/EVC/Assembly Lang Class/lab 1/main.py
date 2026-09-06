"""
This is a program that converts binary or decimal into decimal, octal, or hex
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
