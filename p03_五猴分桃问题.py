
def get_peaches(monkeys):
    peaches = 1
    while not distribute(monkeys, peaches):
        peaches += 5
    return peaches

def distribute(monkeys, peaches):
    for _ in range(monkeys):
        peaches -= 1
        if peaches % 5 != 0:
            return False
        peaches = peaches / 5 * 4
    return True


if __name__ == '__main__':
    print(get_peaches(5))