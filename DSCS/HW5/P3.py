def P3(filename: str) -> list:
    ##### Write your Code Here #####
    with open('C:/Users/seung/OneDrive/바탕 화면/workspace/DSCS/HW5/' + filename, 'r') as file:
        ret = [line for line in file.readlines()
               if len(line) >= 1 and line[0] != '#' and len(line) >= 2 and line[:2] != '//']
    return ret
    ##### End of your code #####


print(P3('alkaline_metals2.txt'))
