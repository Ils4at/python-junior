import re


list_t = []
with open('log.txt', 'r') as f:
    for i in f:
        list_t.append(f.readline())
f.close()


def found_error(list_st: list):
    for item in list_st:
        if re.search('error', item.lower()):
            yield item


result = found_error(list_t)
for i in result:
    print(i)
