from library_games import *
from stats_tools_lib import *
from time import time

start = time()
stats_analysis(1000,elimination_guess_test,elimination_guess_test,True,True,True)
end = time()
print(round(end - start,2))