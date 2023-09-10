

def reversed(number):
    newNumber = 0
    if isinstance(number, int) :
        while number != 0:
            digit = number % 10
            newNumber = newNumber *10+digit
            number = number // 10
    return newNumber

def formatter(number):
    formatterList = []
    if isinstance(number, int):
        binaryNumber = bin(number)
        octalNumber = oct(number)
        formatterList.append(binaryNumber)
        formatterList.append(octalNumber)
    return formatterList



