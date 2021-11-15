from random import randint

score = 0
pogingen = 0

while True:
    n1 = randint(2, 10)
    n2 = randint(2, 10)
    print('Wat is het product van volgende getallen?\n', n1, n2)
    pogingen = pogingen+1
    try:
        answer = int(input('product: '))
    except ValueError:
        print('Ongeldig getal')
        exit()
    except KeyboardInterrupt:
        print('Bedankt en tot volgende keer!')
        exit()
    product = n1 * n2
    if answer == product:
        print('Gefeliciteerd!')
        score = score+1
    else:
        print('Het juiste antwoord was', product)
    if pogingen == 10:
        print('score'/10)
    else:
        break
