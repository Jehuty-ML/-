'''
#while True适合达到一定条件就break，结合利用只有一个打开flag开关，当flag开关次数达到一定时break
'''

import random


def get_out(prisoners):
    monitors = prisoners - 1
    light = False
    count = 0
    while True:
        luck = random.randint(1, prisoners)
        print('number %s is luck today' % luck)
        if luck < monitors:
            if not light:
                light = True
        if luck == monitors:
            if light == True:
                if count == prisoners - 1:
                    print('all is luck')
                    break
                print('-------------------monitor is luck today------------------------')
                light = False
                count += 1




if __name__ == '__main__':
    get_out(4)