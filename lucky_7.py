#OlegPuchkov
import random
def roll_die():
    return random.randint(1, 6)

frequencies = []

def count_until_seven():
    roll1 = roll_die()
    roll2 = roll_die()
    total = roll1 + roll2
    if total != 7:
        print (total)
        frequencies[total] += 1
    else:
        return frequencies[total]
    return
for repeat in range(1000):
    frequencies[repeat] = 0
    
for repeat in range(1000):
    count_until_seven()
    if  frequencies[7]==0:
        break
average = sum(frequencies)/len(frequencies)
print ("The average number of rolls until one gets a 7 is", average)
    
    
