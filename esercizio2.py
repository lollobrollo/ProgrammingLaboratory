def sum_list(list):
    if len(list) == 0:
        return None
    tmp = 0
    for item in list:
      tmp += item
    return tmp