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

def reverse_difference(s1,s2): #same as s1.difference_update(s2) but the complexity depends on s2
    for elem in s2:
        s1.discard(elem)


def listtoint(li):
    n = len(li)
    digit = 10 ** (n-1)
    intret = 0
    for i in li:
        intret += digit * i
        digit //= 10
    return intret

def howmanynumbers(start):
    i = 0
    while start <= 9876:
        if alldigitsdifferent(start): i += 1
        start += 1
    return i


def map_override(li,fun):
    listret = []
    for i in li:
        listret.append(fun(i))
    return listret


def permutations(li):
    n = len(li)
    digit = 10 ** (n-1)
    if n == 0:
        return []
    if n == 1:
        return [li[0]]
    lisret = []
    for i in range(n):
        licop = li.copy()
        elem = licop.pop(i)*digit 
        lisbuff = map_override(permutations(licop),lambda a: elem + a)
        lisret += lisbuff
    return lisret


