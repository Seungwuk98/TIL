def P6(dct1: dict, dct2: dict) -> dict:
    ### Write code here ###
    ret = {}
    for key in dct1:
        if key in dct2 and dct1[key] == dct2[key]:
            if key not in ret:
                ret[key] = []
            ret[key].append(dct1[key])
    return ret

    ### End of your code ###


sample_case = [
    [{'a': 1, 'b': True, 'c': [1, 2]}, {'a': 1, 'b': 123, 'c': [1, 2]}],
    [{'a': 1, 'b': True}, {'c': 1, 'd': 123, 'e': [1, 2]}],
    [{}, {'c': 1, 'd': 123, 'e': [1, 2]}],
    [{1: 1, 2: 2, 3: 3, 4: 4}, {1: 1, 'a': 2, '3': 4, '4': 4}],
    [{123: 1}, {}],
    [{1: 2, 2: 3, 3: 4, 4: 5, 5: 6}, {'a': 1, 'b': 2, '3': 'c', 4: 5, 1:
                                      2}],
    [{1.1: 1, 2.1: 2, 3.1: 3, 4.1: 4}, {1: 1.1, 2: 2.1, 3: 3.1, 4: 4.1,
                                        1.1: 1}],
    [{(1, 2): 'a', (2, 1): 'b', 'c': 4}, {'c': 1, (2, 1): 'b', (1, 2): 'b'}],
    [{1.1: 1, 2.1: 1, 'a': 1, 'b': 1, ('1,2', 3): 1}, {1: 1, 2.1: 1, (3,
                                                                      '1.2'): 1, (1.2, 3): 1, 'a': 1}],
    [{'data': 'science', 'gs': 'ds', (1, 2): 2}, {'data': 'sceince', 'ds':
                                                  'gs', (2, 1): 2}]
]

for test in sample_case:
    print(P6(test[0], test[1]))

print(P6({'a': 1, 'b': True, 'c': [1, 2]}, {'a': 1, 'b': 123, 'c': [1, 2]}))
