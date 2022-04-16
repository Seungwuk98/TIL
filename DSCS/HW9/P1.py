import sys
input = sys.stdin.readline


def P1(parentheses: str) -> bool:
    ##### Write your Code Here #####
    s = []
    for x in parentheses:
        if x == '(' or x == '[' or x == '{':
            s.append(x)
        elif x == ')':
            if s and s[-1] == '(':
                s.pop()
            else:
                return False
        elif x == ']':
            if s and s[-1] == '[':
                s.pop()
            else:
                return False
        elif x == '}':
            if s and s[-1] == '{':
                s.pop()
            else:
                return False
    if s:
        return False
    return True

    ##### End of your code #####
