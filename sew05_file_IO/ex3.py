import csv

dir = './home'
file_name = 'favorite_colors.csv'
favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
]


def write_colors(dir: str, file_name: str, colors: list[dict[str, str]]):
    with open(f"{dir}/{file_name}", "w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "favorite_color"], delimiter=";")
        writer.writeheader()
        for color in colors:
            writer.writerow(color)


if (__name__ == "__main__"):
    write_colors(dir, file_name, favorite_colors)
