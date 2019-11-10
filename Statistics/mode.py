def mode(num):
    dict_num = {}
    for i in range(len(num)):
        if num[i] in dict_num.keys():
            dict_num[num[i]] += 1
        else:
            dict_num.setdefault(num[i], 1)
    max_key = []
    m = max(dict_num.values())
    for k, v in dict_num.items():
        if m == v:
            max_key.append(k)
    return max_key
