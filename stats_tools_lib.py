from library_games import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class GameError(Exception):
    def __init__(self):
        self.message = "the result of a game shouldn't be this"
        super().__init__(self.message)
        
def mean(l):
    le = len(l)
    con = 0
    for i in l:
        con += i
    if le == 0:
        return 0 #undefined for 0 but kept as 0 for practical reasons
    return round(con/le,2) 
                 
def standard_deviation(l):
    n = len(l)
    if n in {0,1}:
        return 0 #undefined for these values but kept as 0 for practical reasons
    meanl = mean(l)
    conret = 0.0
    for i in l:
        ximinu = i - meanl
        conret += ximinu ** 2
    return round(np.sqrt(conret / (n-1)),2)

def exceptional_results(l):
    lsomewhat = []
    lconsiderably = []
    ltruly = []
    meanl = mean(l)
    stdevl = standard_deviation(l)
    for i in l:
        diff = abs(meanl - i)
        if diff >= stdevl and diff < 2 * stdevl:
            lsomewhat.append(i)
        elif diff >= 2 * stdevl and diff < 3 * stdevl:
            lconsiderably.append(i)
        elif diff >= 3 * stdevl:
            ltruly.append(i)
    return (lsomewhat,lconsiderably,ltruly)


def func_analysis(n, fun1, fun2):
    lisf1 = []
    lisf2 = []
    draws = []
    for i in range(n):
        (turns, f1, f2) = computer_vs_computer_test(fun1, fun2, False)
        if f1 and not f2:
            lisf1.append(turns)
        if f2 and not f1:
            lisf2.append(turns)
        if f1 and f2:
            draws.append(turns)
        if not (f1 or f2):
            raise GameError()
    return (lisf1,lisf2,draws)

def stats_analysis(n,fun1,fun2,avg = False,st_dev = False,exceptional_values = False,plots = False):
    (l1,l2,draws) = func_analysis(n,fun1,fun2)
    fun1name = fun1.__name__
    fun2name = fun2.__name__
    prgame1 = fun1name+" won " + str(len(l1)) + " times"
    prgame2 = fun2name+" won " + str(len(l2)) + " times"
    prdraw = str(len(draws)) + " games were drawn"
    if avg:
        mean1 = mean(l1)
        mean2 = mean(l2)
        meandraws = mean(draws)
        prgame1 += ", it took " +str(mean1) +" turns on average"
        prgame2 += ", it took " +str(mean2) +" turns on average"
        prdraw += " in " + str(meandraws) +" turns on average"
    if st_dev:
        stdev1 = standard_deviation(l1)
        stdev2 = standard_deviation(l2)
        stdevdraws = standard_deviation(draws)
        prgame1 += ", with a standard deviation of " + str(stdev1)
        prgame2 += ", with a standard deviation of " + str(stdev2)
        prdraw += ", with a standard deviation of " + str(stdevdraws)
    if exceptional_values:
        (some1,cons1,tru1) = exceptional_results(l1)
        (some2,cons2,tru2) = exceptional_results(l2)
        (somed,consd,trud) = exceptional_results(draws)
        prgame1 += "\n exceptional values are " + str(some1) +" (somewhat) " + str(cons1) + " '(considerably) " + str(tru1) + " (truly) "
        prgame2 += "\n exceptional values are " + str(some2) +" (somewhat) " + str(cons2) + " '(considerably) " + str(tru2) + " (truly) "
        prdraw += "\n exceptional values are " + str(somed) +" (somewhat) " + str(consd) + " '(considerably) " + str(trud) + " (truly) "
    print("analysis was made for " + str(n) + " games using " + fun1name + " and " + fun2name)
    print(prgame1)
    print(prgame2)
    print(prdraw)
    (_,axe) = plt.subplots(1,3,figsize=(18,4))
    axe[0].hist(l1)
    axe[1].hist(l2)
    axe[2].hist(draws)
    if plots:
        plt.tight_layout()
        plt.show()


        

                

		
    
