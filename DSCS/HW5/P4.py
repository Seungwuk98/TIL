def P4(filename: str) -> list:
    ##### Write your Code Here #####
    ret = []
    with open('C:/Users/seung/OneDrive/바탕 화면/workspace/DSCS/HW5/' + filename, 'r') as file:
        for line in file.readlines():
            line_length = len(line)
            if (line_length >= 1 and line[0] == '#') or (line_length >= 2 and line[:2] == '//'):
                continue
            for i in range(line_length):
                if line[i] == '#' or (i < line_length-1 and line[i] == line[i+1] == '/'):
                    break
            ret.append(line[:i].strip())
    return ret
    ##### End of your code #####


print(P4('alkaline_metals2.txt'))
