import os
import argparse
import json

parser = argparse.ArgumentParser(description='Find large files in a directory')

parser.add_argument('--root', '-r', type=str, help='The root directory to start the search from')
parser.add_argument('--min', '-m', type=int, help='The minimum size of files to search for')
parser.add_argument('--output', '-o', type=str, help='The name of the file to write the results to')
parser.add_argument('--sort', '-s', action='store_true', help='Sort the output by file size')

args = parser.parse_args()

root_directory = args._get_kwargs()[0]
min_size = args._get_kwargs()[1]
output_filename = args._get_kwargs()[2]
sort = args._get_kwargs()[3]

large_files = []

for dirpath, dirnames, filenames in os.walk(root_directory[1]):
  for filename in filenames:
    file_path = os.path.join(dirpath, filename)
    file_size = os.path.getsize(file_path)
    if file_size > min_size[1]:
      large_files.append({
        "file_path": file_path,
        "file_size": file_size
      })
      

if sort[1] == True:
    large_files = sorted(large_files, key=lambda x: x['file_size'])

with open(f'json/{output_filename[1]}', 'w') as output_file:
  json.dump(large_files, output_file, indent=4, sort_keys=True)

import time

def main():
    start_time = time.perf_counter()
    
    # here comes the code you want to measure its runtime

    stop_time = time.perf_counter()
    print(f"Measured time: {stop_time - start_time:0.4f} seconds")



if __name__ == "__main__":
    main()
