def game(number):
    strNumber = str(number)

    if (strNumber[1] > strNumber[0]):
        result = int(strNumber[1]) - int(strNumber[0])

    else:
        result = int(strNumber[0]) - int(strNumber[1])

    return result