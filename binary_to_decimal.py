def binary_to_decimal(integer,frac):
    counter = 0
    #for the integer part (RHS) of the conversion
    #starts at exponent 0
    value=0.0
    for x in integer[::-1]:
        value += int(x)*(2**counter)
        counter +=1
    counter=-1
    for y in frac:
        value += int(y)*(2**counter)
        counter -= 1
    return value
    
#this was just to test
user_input = input("Enter a binary number: ").strip()

if "." in user_input:
    integer, frac = user_input.split(".")
else:
    integer, frac = user_input, ""

print(binary_to_decimal(integer, frac))
