import random

sweepstakes_contestants = {

    1: 'Austin Flatt',
    2: 'Ella Anderson',
    3: 'Hali Flatt',
    4: 'Tre Tardy',
    5: 'Aaron K'
}


def sweepstakes_winner():
    print('The sweepstakes winner is', sweepstakes_contestants[random.randint(0, 5)])