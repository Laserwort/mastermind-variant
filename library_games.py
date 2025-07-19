#libraries
from random import randint,choice
from theorycrafting import *

#global variables:
prevrounds_user = dict() #k = int : v = (int,(int,int))
prevrounds_computer = dict() #k = int: v = (int,(int,int))
all_numbers = {listtoint([i,j,k,m]) for i in range(1,10) for j in range(10) for k in range(10) for m in range(10) if i != j and i != k and i != m and j != k and j != m and k != m}

#classes

class InputError(Exception):
    def __init__(self, message="too many failed entries"):
        self.message = message
        super().__init__(self.message)

#functions

def inttolistint(number: int):
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

def alldigitsdifferent(number: int):
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

def guess_eval(i1,i2):
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

def worst_guess(prevrounds):
    guess = random4digitgen()
    while guess in prevrounds:
        guess = worst_case()
    return guess

def worst_guess_test(all,prevrounds):
    guess = random4digitgen()
    while guess in prevrounds:
        guess = worst_case()
    return guess
    

def worst_case():
    number = 1023
    while not alldigitsdifferent(number) and number < 9876:
        number += 1
    if number == 9876:
        return 1023
    return number

def guess_eval_add(tu):
    (minus,plus) = tu
    return plus - minus

    
def elimination_guess(prevrounds):
    #elimination
    global all_numbers
    val = 0
    to_remove = set()
    for k in prevrounds:
        if val < k:
            val = k
    if val > 0:
        (n,tu) = prevrounds[val]
        for num in all_numbers:
            if guess_eval(num,n) != tu:
                to_remove.add(num)
    all_numbers = all_numbers.difference(to_remove)
    #guess
    guess = choice(list(all_numbers))
    all_numbers.remove(guess)
    return guess


def elimination_guess_test(all,prevrounds):
    #elimination
    val = 0
    to_remove = set()
    for k in prevrounds:
        if val < k:
            val = k
    if val > 0:
        (n,tu) = prevrounds[val]
        for num in all:
            if guess_eval(num,n) != tu:
                to_remove.add(num)
    all.difference_update(to_remove)
    #guess
    guess = choice(list(all))
    all.remove(guess)
    return guess


    

def player_game(func):
    print("choose your number: ")
    usernumber = userentry()
    computernumber = random4digitgen()
    gi = 0
    while True: #game itself
        while True: #player decision
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
            gtup = guess_eval(u_entry,computernumber)
            print(gtup)
            tuapp = (u_entry,gtup)
            prevrounds_user[gi] = tuapp
            print("computer's turn")
            print("your number is " + str(usernumber))
            comguess = func() # <- first-order variable
            cgtup = guess_eval(comguess,usernumber)
            print("computer's guess is "+ str(comguess))
            print(cgtup)
            prevrounds_computer[gi] = (comguess,cgtup)
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


def computer_vs_computer(func1,func2,print_the_results):
    c1n = random4digitgen()
    c2n = random4digitgen()
    prevrounds_computer1 = dict() #k = int: v = (int,(int,int))
    prevrounds_computer2 = dict() #k = int: v = (int,(int,int)) 
    r = 0
    f1won = f2won = False
    while True:
        r += 1
        c1_guess = func1(prevrounds_computer1)
        cg1_tup = guess_eval(c1_guess,c2n)
        c2_guess = func2(prevrounds_computer2)
        cg2_tup = guess_eval(c2_guess,c1n)
        prevrounds_computer1[r] = (c1_guess,cg1_tup)
        prevrounds_computer2[r] = (c2_guess,cg2_tup)
        if cg1_tup == (0,4) and cg2_tup != (0,4):
            if print_the_results:
                print("the first function won")
            f1won = True
            break
        if cg2_tup == (0,4):
            if print_the_results:
                print("the second function won")
            f2won = True
            break
        if cg1_tup == (0,4) and cg2_tup == (0,4):
            if print_the_results:
                print("it's a draw")
            f1won = f2won = True
            break
    if print_the_results:
        print("after " + str(r) + " rounds")
    return (r,f1won,f2won)

def computer_vs_computer_test(func1,func2,print_the_results):
    prevrounds_computer1 = dict() #k = int: v = (int,(int,int))
    prevrounds_computer2 = dict() #k = int: v = (int,(int,int)) 
    all_no1 = {listtoint([i,j,k,m]) for i in range(1,10) for j in range(10) for k in range(10) for m in range(10) if i != j and i != k and i != m and j != k and j != m and k != m}
    all_no2 = {listtoint([i,j,k,m]) for i in range(1,10) for j in range(10) for k in range(10) for m in range(10) if i != j and i != k and i != m and j != k and j != m and k != m}
    c1n = random4digitgen()
    c2n = random4digitgen()
    r = 0
    f1won = f2won = False
    while True:
        r += 1
        c1_guess = func1(all_no1,prevrounds_computer1)
        cg1_tup = guess_eval(c1_guess,c2n)
        c2_guess = func2(all_no2,prevrounds_computer2)
        cg2_tup = guess_eval(c2_guess,c1n)
        prevrounds_computer1[r] = (c1_guess,cg1_tup)
        prevrounds_computer2[r] = (c2_guess,cg2_tup)
        if cg1_tup == (0,4) and cg2_tup != (0,4):
            if print_the_results:
                print("the first function won")
            f1won = True
            break
        if cg2_tup == (0,4) and cg1_tup != (0,4) :
            if print_the_results:
                print("the second function won")
            f2won = True
            break
        if cg1_tup == (0,4) and cg2_tup == (0,4):
            if print_the_results:
                print("it's a draw")
            f1won = f2won = True
            break
    if print_the_results:
        print("after " + str(r) + " rounds")
    return (r,f1won,f2won)

        


