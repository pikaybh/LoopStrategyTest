import random

N = 100
numbers = [i for i in range(100)]

random.shuffle(numbers)
summation = 0.0

print("[INFO]  This script is based on idea of Veritasium.\n\tThe main idea of this mathmatical blah blah...")

while(True):
    big_enough_num = input("[INFO]  Type a number that is big enough, at list 10,000: ")
    if (big_enough_num == ''):
        print("[INFO]  Operating process for 10,000 times...")
        big_enough_num = 10000
        break
    big_enough_num = int(big_enough_num)
    if (big_enough_num >= 10000):
        break
    print("[INFO]  Not big enough!")

big_enough_float = float(str(big_enough_num) + ".0")

if (big_enough_num > 100000):
    print("[INFO]  This process might damage your CPU...")

for k in range(big_enough_num):
    random.shuffle(numbers)
    is_good = True
    for i in range(100):
        my_num = i
        is_flag = False
        for j in range(50):
            if numbers[my_num] == i:
                is_flag = True
                break
            my_num = numbers[my_num]
        if is_flag == False:
            is_good = False
            break
    if is_good == True:
        summation +=1.0
        
result = summation / big_enough_float
print("[INFO]  Result: ", result)