def count_tokens(s:str) -> dict:
    s = s.split()
    tokens = {}
    for i in s:
        if i in tokens:
            tokens[i] += 1
        else:
            tokens[i] = 1
    return tokens