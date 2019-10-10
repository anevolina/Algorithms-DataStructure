
def towerOfHanoi(From, To, Additional, Number):

    if Number <= 0:
        return

    towerOfHanoi(From, Additional, To, Number-1)
    print('Move {} disk from {} to {}'.format(Number, From, To))
    towerOfHanoi(Additional, To, From, Number-1)

towerOfHanoi('A', 'C', 'B', 10)
