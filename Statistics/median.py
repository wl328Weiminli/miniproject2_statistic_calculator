def median(num):
    list_num = [num[i] for i in range(len(num))]
    list_num.sort()
    l_num = len(num)
    if l_num % 2 == 1:
        i = int((l_num + 1) / 2) - 1
        return list_num[i]
    else:
        i = int(l_num / 2) - 1
        return (list_num[i] + list_num[i + 1]) / 2
