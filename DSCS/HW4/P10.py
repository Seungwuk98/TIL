def P10(words: set, query_word: str) -> bool:
    ### Write code here ###
    n = len(query_word)
    for word in words:
        if len(word) == n:
            chk = 0
            for i in range(n):
                if query_word[i] != word[i]:
                    chk += 1
                    if chk > 1:
                        break
            if chk == 1:
                return True
    return False

    ### End of your code ###


sample_case = [
    [{"data", "science", "datt"}, "data"],
    [{"data", "science", "dddaa"}, "daaa"],
    [{"data", "science", "dddaa"}, "aata"],
    [{"data", "science", "snu", "scienzz"}, "scienzz"],
    [{"data", "science", "snu", "yourim"}, "yoorim"],
    [{"graduate", "school", "of", "data", "science", "computing", "for"},
        "graduat"],
    [{"pizza", "pasta", "drink", "chikken", "chicken", "chiken", "food"},
        "chicken"],
    [{"pizza", "pasta", "drink", "chikken", "chicken", "chiken", "food"},
        "pizzaa"],
    [{"soccer", "basketball", "baseball", "basketbool", "volleyball",
      "bolleyball"}, "vaolleyball"],
    [{"soccer", "basketball", "baseball", "basketbool", "volleyball",
      "bolleyball"}, "basketball"]
]
for test in sample_case:
    print(P10(test[0], test[1]))
