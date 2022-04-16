def P2(filename: str) -> list:
    ##### Write your Code Here #####
    with open('C:/Users/seung/OneDrive/바탕 화면/workspace/DSCS/HW5/' + filename, 'r') as file:
        ret = [line for line in file.readlines()]
    return ret[::-1]
    ##### End of your code #####


print(P2('alkaline_metals.txt'))
