def P10(rat_1: list, rat_2: list, measure_day: int) -> bool:
    is_greater = 0
    ##### Modify code Here #####
    is_greater = rat_1[measure_day-1] > rat_2[measure_day-1]
    ##### End of your code #####
    return is_greater
