from random import randint

class InputError(Exception):
    def __init__(self, message="too many failed entries"):
        self.message = message
        super().__init__(self.message)



def inttolistint(number):
    listret = []
    while number != 0:
        listret.append(number % 10)
        number //= 10
    listret.reverse()
    return listret

def random4digitgen():
    max = 9
    digit = 1000
    listt = list(range(1,10))
    randno = randint(0,max-1)
    numret = listt[randno] * digit
    listt.pop(randno)
    max -= 1
    listt.insert(0,0)
    while digit != 0:
        digit //= 10
        randno = randint(0,max-1)
        numret += listt[randno] * digit
        listt.pop(randno)
        max -= 1
    return numret

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

def userentry():
    print("Enter a 4 digit number, each digit must be different")
    i = 0
    j = 0
    while i < 10:
        while j < 10:
            try:
                user_input = int(input())
                break
            except ValueError:
                print("That's not a valid integer. Please try again.")
                j += 1
        if alldigitsdifferent(user_input):
            break
        else:
            print("digits are not different and/or the number is not 4 digit")
            i += 1
    if i == 10 or j == 10:
        raise InputError("too many failed entries")
    return user_input

def guess(i1,i2):
    contains = 0
    samedigit = 0
    li1 = inttolistint(i1)
    li2 = inttolistint(i2)
    i = 0
    while i < len(li1):
        if li1[i] == li2[i]:
            samedigit += 1
            li1.pop(i)
            li2.pop(i)
            continue
        i += 1
    si1 = set(li1)
    for i in li2:
        if i in si1:
            contains -= 1
    return (contains,samedigit)

def worst_case(number):
    number += 1
    while not alldigitsdifferent(number) and number < 9876:
        number += 1
    if number == 9876:
        return 1023
    return number

def guessadd(tu):
    (minus,plus) = tu
    return plus - minus
""""
def algorithmp1(potent,prevres):
    if 1234 not in prevres:
        return 1234
    if prevres[1234] == (0,0):
        potent -= set(inttolistint(1234))
    if 5678 not in prevres:
        return 5678
    if prevres[5678] == (0,0):
        potent -= set(inttolistint(5678))
    if guessadd(prevres[1234]) + guessadd(prevres[5678]) == 4:
        potent -= {0,9}
    
    lpotent = list(potent)
    lpotent.sort()
    digit = 1000
    max = len(lpotent)
    if 0 in potent:
        lpotno0 = lpotent.copy()
        lpotno0.remove(0)
        maxalt = max - 1
        numret +=  * digit
        digit //= 10
    while digit != 0:
        digit //= 10
        
        numret +=  * digit
        lpotent.pop(randno)
        max -= 1
    if numret not in prevres:
        return numret
    else:
"""     
def randomgame():
    print("choose your number: ")
    usernumber = userentry()
    computernumber = random4digitgen()
    gi = 0
    prevrounds_user = dict() #k = int : v = (int,(int,int))
    prevrounds_computer = dict() #k = int: v = (int,int) different than prevrounds_user
    while True:
        while True:
            print("what are you going to do? (1: next round, 2: see the result of the previous rounds,3: quit game)")
            try:
                decision = int(input())
                if decision <= 0 or decision > 3:
                    print("not an potion")
                else:
                    break
            except ValueError:
                print("That's not a valid integer. Please try again.")
        if decision == 1:
            gi += 1
            print("make a guess: ")
            while True:
                u_entry = userentry()
                i = 0
                for k,v in prevrounds_user.items():
                    if v == u_entry:
                        print("you've already guessed that number at round " + str(i+1)+", try again")
                    else:
                        i += 1
                if i == len(prevrounds_user):
                    break
            gtup = guess(u_entry,computernumber)
            print(gtup)
            tuapp = (u_entry,gtup)
            prevrounds_user[gi] = tuapp
            print("computer's turn")
            print("your number is " + str(usernumber))
            comguess = random4digitgen()
            while comguess in prevrounds_user:
                comguess = worst_case(comguess)
            cgtup = guess(comguess,usernumber)
            print("computer's guess is "+ str(comguess))
            print(cgtup)
            prevrounds_computer[comguess] = cgtup
        if decision == 2:
            for k,v in prevrounds_user.items():
                (f,s) = v
                print("round no: "+ str(k)+" number: "+str(f)+" result: " + str(s))
            print("1 to take a look at a particular integer, 2 to continue")
            while True:
                try:
                    dec = int(input())
                    if dec == 2 or dec == 1:
                        break
                    else:
                        print("input should be 1 or 2")
                except ValueError:
                    print("That's not a valid integer. Please try again.")
            if dec == 1:
                while True:
                    try:
                        flag = True
                        print("which number?") 
                        round = userentry()
                        for k,v in prevrounds_user.items():
                            (f,s) = v
                            if f == round:
                                flag = False
                                print("round no: "+ str(k)+" number: "+str(f)+" result: " + str(s))
                                break
                        if flag:
                            print("that number has never been tried")
                        break
                    except ValueError:
                        print("That's not a valid integer. Please try again.")
            continue
        if decision == 3:
            print("game abandoned")
            break
        if cgtup == (0,4) and gtup != (0,4):
            print("you've lost")
            break
        if gtup == (0,4) and cgtup == (0,4):
            print("draw")
            break
        if gtup == (0,4):
            print("you've won")
            break
    print("computer's number was "+str(computernumber))


randomgame()

