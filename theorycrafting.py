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

def listtoint(li):
    n = len(li)
    digit = 10 ** (n-1)
    intret = 0
    for i in li:
        intret += digit * i
        digit //= 10
    return intret

def push(la,li,a,b): #carries element a of li to element j of li (if a < b otherwise its unaffected)
    for i in range(a,b-1):
        la.append(listtoint(li))
        li[i],li[i+1] = li[i+1],li[i]



def permutations_broken(li):
    n = len(li)
    lisret = []
    for i in range(n):
        if i == 0:
            for j in range(n-1):
                push(lisret,li,1,n)
        else:
            li[0],li[i] = li[i],li[0]
            for j in range(n-1):
                push(lisret,li,1,n)
    return (lisret,len(lisret))

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


