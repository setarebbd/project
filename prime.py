
hads = int(input('gess one number : '))

aval = True

for i in range(2, hads):
    if hads % i == 0:
        aval = False
if aval:
    print('aval ast')
else:
    print('aval nist')
