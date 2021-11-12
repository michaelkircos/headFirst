from datetime import datetime
import time
import random

def odd_minute():									## I decided to make a function to handle the determination of whether the minute was odd/even.
    right_this_minute = datetime.today().minute
    if right_this_minute % 2 != 0 :                 ## Instead of using a list containing all of the odd minute values I used modulo with a 
        print("This minute seems a little odd.")    ## comparison operator
    else:
        print("Not an odd minute.")


for i in range(5):
    if i < 4:
        odd_minute()
        wait_time = random.randint(1, 60)
        print("You have " + str(wait_time) + " seconds until it's time to decide again.")
        time.sleep(wait_time)
    elif i == 4:
        odd_minute()
        print("Singularity achieved!")
    else:
        print("I don't know WTF is going on :( ")
    