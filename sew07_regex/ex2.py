import re
import requests
import argparse

parser = argparse.ArgumentParser(description='Extract URLs from a website')

parser.add_argument('--url', '-u', type=str,
                    help='The URL to extract URLs from')

args = parser.parse_args()

url = args._get_kwargs()[0]
url = url[1]

# Sending a GET request to the URL and receive the response
response = requests.get(url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Processing the content
    print("Content downloaded successfully")
else:
    print('Failed to download content. Status code:', response.status_code)


def extract_urls(url):
    # https?://                    # Matches "http://" or "https://" | "s" is optional.
    # (?:[-\w.]|(?:%[\da-fA-F]{2}))+
    # (?: ... )                    # Non-capturing group for grouping without capturing.
    # [-\w.]                       # Matches any character that is a hyphen, word character (letter, digit, underscore), or period.
    # |                            # OR
    # (?:%[\da-fA-F]{2})           # Another non-capturing group that matches URL-encoded characters, like "%20" (space).
    # +                            # Ensures that the sequence repeats one or more times.
    urls = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)
    return urls


def count_urls(url):
    list = []
    urls = extract_urls(str(url.content))
    for url in urls:
        if url not in list:
            list.append(url)
    print(len(list))
    print(list)


if __name__ == "__main__":
    count_urls(response)
