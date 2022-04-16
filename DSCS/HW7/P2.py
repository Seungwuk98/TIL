def P2(s: str) -> int:
    ### Modify code here ###
    d = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    num = ''
    st = ''
    for x in s:
        if '0' <= x <= '9':
            num += x
        else:
            st += x
            if st in d:
                num += d[st]
                st = ''
    return int(num)
    ### End of your code ###
