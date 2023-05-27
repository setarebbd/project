while True:
    import random
    options = ['rock', 'scissors', 'paper']
    cpu = random.choice(options)
    p1 = input('write  rock/paper/scissors: ')
    print('cpu: ', cpu)

    if p1 == 'rock' and cpu == 'scissors':
        print('p1 win')
    elif p1 == 'rock' and cpu == 'paper':
        print('cpu win')
    elif p1 == 'rock' and cpu == 'rock':
        print('try again')
    elif p1 == 'paper' and cpu == 'rock':
        print('p1 win')
    elif p1 == 'paper' and cpu == 'scissors':
        print('cpu win')
    elif p1 == 'paper' and cpu == 'paper':
        print('try again')
    elif p1 == 'scissors' and cpu == 'rock':
        print('cpu win')
    elif p1 == 'scissors' and cpu == 'paper':
        print('p1 win')
    elif p1 == 'scissors' and cpu == 'scissors':
        print('try again')
