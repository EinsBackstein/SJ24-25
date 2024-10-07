def remove_vowels(s:str)->str:
    return s.translate({ord(i): None for i in 'AEIOUaeiou'})

if(__name__ == "__main__"):
    remove_vowel = input("Please input a string: ")
    print(remove_vowels(remove_vowel))