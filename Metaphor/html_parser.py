
from bs4 import BeautifulSoup
import json
def remove_tags(html):
 
    # parse html content
    soup = BeautifulSoup(html, "html.parser")
 
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
 
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)

# with open('content.json', 'r') as file:
#     file_contents = json.load(file)

# item = file_contents[0]
# print(remove_tags(item['Extract']))