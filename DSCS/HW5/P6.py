def P6(input_filename: str, out_filename: str):
    ##### Write your Code Here #####
    with open('C:/Users/seung/OneDrive/바탕 화면/workspace/DSCS/HW5/' + input_filename, 'r') as file:
        ret = [line.strip().split()for line in file.readlines()]
    with open('C:/Users/seung/OneDrive/바탕 화면/workspace/DSCS/HW5/' + out_filename, 'w') as file:
        for line in ret:
            file.write(','.join(line) + '\n')
    ##### End of your code #####


P6('alkaline_metals.txt', 'output.txt')
