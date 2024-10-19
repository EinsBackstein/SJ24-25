path = "./home/favorite_colors.csv"
import csv

def read_colors(path: str) -> list[dict[str, str]]:
  with open(path, encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")
    return list(reader)

def print_colors(colors: list[dict[str, str]]) -> None:
  # "table" header
  columns = colors[0].keys()
  print("| " + "\t| ".join(columns) + "|")
  print("| " + "\t| ".join("---" for pos in columns) + "\t|")
  
  # favorite colors / table rows
  for color in colors:
    print("|" + "\t| ".join(color[pos] for pos in columns) + "\t|")

if __name__ == "__main__":
    favorite_colors = read_colors(path)
    print_colors(favorite_colors)