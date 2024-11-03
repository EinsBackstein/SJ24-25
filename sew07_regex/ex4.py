import re
import json
import os

def extract_data_from_file():
    data = []
    with open('test.txt','r') as f:
        content = f.read()
        for line in content.split('\n'):
                # Date: - mathches the string "Date: "
                # ?P<Date>\d{4}-\d{2}-\d{2}) - matches a date in the format "YYYY-MM-DD" and stores it in a group named "Date"
                match = re.match(r'Date: (?P<Date>\d{4}-\d{2}-\d{2})', line)
                if match:
                  current_entry = match.groupdict()
                  data.append(current_entry)
                  continue
                # Name: - matches the string "Name: "
                # ?P<Name>.+ - matches any character one or more times and stores it in a group named "Name"
                match = re.match(r'Name: (?P<Name>.+)', line)
                if match:
                  current_entry.update(match.groupdict())
                  continue
                # Phone: - matches the string "Phone: "
                # ?P<Phone>[\d\s-]+ - matches any digit, whitespace or hyphen one or more times and stores it in a group named "Phone"
                match = re.match(r'Phone: (?P<Phone>[\d\s-]+)', line)
                if match:
                  current_entry.update(match.groupdict())
                  continue
        return data

with open('json/output.json', 'w') as f:
    json.dump(extract_data_from_file(), f, indent=4)

print(extract_data_from_file())