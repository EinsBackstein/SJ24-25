def is_prime(n: str | int) -> bool:
    if(n.isdigit() == False):
        exit('NaN')
    n = int(n)
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

if(__name__ == "__main__"):
    check_prime = input("Please input a number: ")
    print(is_prime(check_prime))
