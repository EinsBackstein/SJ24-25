def count_tokens(s:str) -> dict:
    s = s.split()
    tokens = {}
    for i in s:
        if i in tokens:
            tokens[i] += 1
        else:
            tokens[i] = 1
    return tokens

if(__name__ == "__main__"):
    count_token = input("Please input a string: ")
    print(count_tokens(count_token))