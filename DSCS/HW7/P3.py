def P3(info: list) -> str:
    ##### Write your Code Here #####
    sex, year, month, day = info
    ret = 1
    if year >= 2000:
        ret += 2
    if sex == 'FEMALE':
        ret += 1
    year %= 100
    ret = str(year*100000 + month*1000 + day*10 + ret)
    return ret if year else '0'*(7-len(ret))+ret
    ##### End of your code #####
