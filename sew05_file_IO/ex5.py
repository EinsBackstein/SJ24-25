import json
dir="./home"
file_name="favorite_colors.json"
favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
]

def load_colors(dir: str, file_name: str):
    with open(f"{dir}/{file_name}", "r", newline="") as file:
      output = json.load(file)
      return output



def dump_colors(dir: str, file_name: str, favorite_colors: list[dict[str, str]]):
    with open(f"{dir}/{file_name}", "w", newline="") as file:
        json.dump(favorite_colors, file)


if __name__ == "__main__":
    dump_colors(dir, file_name, favorite_colors)
    print(load_colors(dir, file_name))