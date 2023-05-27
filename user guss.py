import random
adad = random.randint(1, 50)
count = 0
while True:

    hads = int(input('in (1,50)hads bzn: '))
    count = count+1
    if hads > 50 or hads < 1 or hads == str:
        print('try again')
    elif hads == adad:
        print('wooow1')
        print('your try count= ', count)
    elif hads > adad:
        print('hadset bozorge')
    elif hads < adad:
        print('hadset kochike')
