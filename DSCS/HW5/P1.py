def P1(filename: str) -> list:
    ##### Write your Code Here #####
    with open('C:/Users/seung/OneDrive/바탕 화면/workspace/DSCS/HW5/' + filename, 'r') as file:
        ret = [line.strip().split()for line in file.readlines()]
    return ret
    ##### End of your code #####


print(P1('alkaline_metals.txt'))
