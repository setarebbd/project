while True:
    hads = int(input('gess one number : '))
    if hads == 2 or hads == 3 or hads == 5 or hads == 7:
        print('aval ast')
    elif hads == 1:
        print('aval nist')
    elif hads % 2 == 0:
        print('aval nist')
    elif hads % 3 == 0:
        print('aval nist')
    elif hads % 5 == 0:
        print('aval nist')
    elif hads % 7 == 0:
        print('aval nist')
    else:
        print('aval ast')
