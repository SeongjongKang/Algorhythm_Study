import re
def solution(files):
    num_sort = sorted(files, key = lambda x : int(re.findall('\d+', x)[0]))
    str_sort = sorted(num_sort, key = lambda x : re.split('\d+',x.lower())[0])
    return str_sort


