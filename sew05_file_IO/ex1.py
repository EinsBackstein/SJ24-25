starships = ["Discovery","Enterprise","Defiant","Voyager"]
path = "./home/starships.txt"

def write_names(path:str, list: list[str]):
    with open(path, "w", encoding="utf-8") as file:
        for name in list:
            file.write(name + "\n")

if(__name__ == "__main__"):
    write_names(path, starships)