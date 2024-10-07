def remove_vowels(s:str)->str:
    return s.translate({ord(i): None for i in 'AEIOUaeiou'})