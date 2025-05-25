def alldigitsdifferent(number):
    if number // 1000 == 0 or number // 10000 != 0:
        return False
    verifset = set()
    while number != 0:
        currentdigit = number % 10
        if currentdigit in verifset:
            return False
        else:
            verifset.add(currentdigit)
        number //= 10
    return True
def howmanynumbers(start):
    i = 0
    while start <= 9876:
        if alldigitsdifferent(start): i += 1
        start += 1
    return i

print(howmanynumbers(1023))