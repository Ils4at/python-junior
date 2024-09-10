def get_numbers():
    list_num = []
    for item in list(range(1000, 2001)):
        if item % 5 != 0 and item % 7 == 0:
            list_num.append(item)
    return list_num

#raise NotImplementedError



