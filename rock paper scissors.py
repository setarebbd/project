while True:
    p1 = input('p1  rock/paper/scissors: ')

    p2 = input('p2  rock/paper/scissors: ')

    if p1 == 'rock' and p2 == 'scissors':
        print('p1 win')
    elif p1 == 'rock' and p2 == 'paper':
        print('p2 win')
    elif p1 == 'rock' and p2 == 'rock':
        print('try again')
    elif p1 == 'paper' and p2 == 'rock':
        print('p1 win')
    elif p1 == 'paper' and p2 == 'scissors':
        print('p2 win')
    elif p1 == 'paper' and p2 == 'paper':
        print('try again')
    elif p1 == 'scissors' and p2 == 'rock':
        print('p2 win')
    elif p1 == 'scissors' and p2 == 'paper':
        print('p1 win')
    elif p1 == 'scissors' and p2 == 'scissors':
        print('p2 win')
