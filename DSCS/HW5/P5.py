def P5(filename: str) -> int:
    ##### Write your Code Here #####
    with open('C:/Users/seung/OneDrive/바탕 화면/workspace/DSCS/HW5/' + filename, 'r') as file:
        ret = [[nline.split('\n')for nline in line.strip().split()]
               for line in file.readlines()]
    return max([max([max([len(white)for white in space]) for space in line])for line in ret])
    ##### End of your code #####


print(P5('alkaline_metals.txt'))
