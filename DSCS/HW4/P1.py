def P1(lst: list) -> set:
    ### Write code here ###
    set1 = set()
    set2 = set()
    for num in lst:
        if num not in set1:
            set1.add(num)
        else:
            set2.add(num)
    return set2

    ### End of your code ###
