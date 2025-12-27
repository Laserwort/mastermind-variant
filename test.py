from library_games import *
from stats_tools_lib import *
from time import time

start = time()
stats_analysis(1000,elimination_guess_test,worst_guess_test,plots = True,exceptional_values=True)
end = time()
print(round(end - start,2))