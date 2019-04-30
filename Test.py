four = 0


def hitler(four):
    four = 2 * 2
    return four

def second(four):
    hitler(four)
    print(hitler(four))

second(four)
