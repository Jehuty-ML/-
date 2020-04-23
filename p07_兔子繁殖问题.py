


# def get_rabbits(month):
#     rabbits = 2
#     if month <= 2:
#         return rabbits
#     else:
#         return get_rabbits(month-1) + get_rabbits(month-2)
#
#
#
#
#
# if __name__ == '__main__':
#     for month in range(1, 12+1):
#         print(get_rabbits(month))





def get_rabbits(month):
    if month==1 or month==2:
        return 2
    else:
        return get_rabbits(month-1) + get_rabbits(month-2)





if __name__ == '__main__':
    for month in range(1, 12+1):
        print(month, get_rabbits(month))









