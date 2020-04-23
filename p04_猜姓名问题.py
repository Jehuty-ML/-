import math

NAMES= '赵钱孙李周吴郑王冯陈褚卫蒋武涵'

def get_rows(NAMES):
    rows = int(math.log(len(NAMES), 2)) + 1
    result = ['' for _ in range(rows)]  #['','','','','',*****]
    id = 1
    for name in NAMES:
        current = id
        for row_id in range(len(result)):
            if current % 2 != 0:
                result[row_id] += name
            current //= 2
        id += 1

    return result


def get_name(answers):  #answers= [1,0,1,0]
    id = 0  #id为0若answers最后一位为0会无法乘以2
    for answer in reversed(answers):
        id *= 2
        if answer:
            id += 1

    return NAMES[id - 1]

if __name__ == '__main__':
    rows = get_rows(NAMES)
    answers = []
    for row in rows:
        print(row)
        answer = input('你猜的姓在不在这一行中？(y, n)')
        if answer is None or len(answer) == 0:
            break
        if answer.lower() in ('y', 'yes'):
            answers.append(True)
        else:
            answers.append(False)
    print('你猜的姓是：', get_name(answers))

