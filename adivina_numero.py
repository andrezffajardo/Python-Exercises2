import random


def run():
    num_aleat = random.randint(1, 100)
    num_eleg = int(input('Escribe un número del 1 al 100: '))
    while num_eleg != num_aleat:
        if num_eleg < num_aleat:
            print('Es un número más grande')
        else:
            print('Es un número más pequeño')
        num_eleg = int(input('Elige otro número: '))
    print('¡Ganaste!')


if __name__ == '__main__':
    run()