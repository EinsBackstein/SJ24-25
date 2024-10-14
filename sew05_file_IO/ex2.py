path = "./home/starships.txt"

def read__names(path:str):
    with open(path, "r", encoding="utf-8") as file:
       content=[]
       for line in file:
            content.append(line.strip())
    return content

def print_names(list: list[str]):
    for str in list:
        print(str)

if(__name__ == "__main__"):
    print_names(read__names(path))