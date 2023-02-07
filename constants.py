BASKET = 211
MAX_TURN = 19
RESULT ={True:"Wp! /reset ?", False: "Got fun? /reset ?"}

seed = 75 # можно подумать где в ui прикрутить переключатель
DIFFICULTY = []
for i in range(seed):
    DIFFICULTY.append(True)
for i in range(100 - seed):
    DIFFICULTY.append(False)