import re
import requests

url = 'https://www.htl-villach.at'

# Sending a GET request to the URL and receive the response
response = requests.get(url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Processing the content
    print("Content downloaded successfully")
else:
    print('Failed to download content. Status code:', response.status_code)



def extract_urls(url):
    
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