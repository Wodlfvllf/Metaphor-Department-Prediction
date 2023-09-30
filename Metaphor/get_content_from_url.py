from metaphor_python import Metaphor
import json
import html_parser
import requests

api_key = 'f4c68fbc-bcbc-4a85-b3f3-8d591adf0020'
metaphor = Metaphor(api_key)

def retrieve_and_save_contents(input_json_file, output_json_file, language):
    with open(input_json_file, 'r') as file:
        file_contents = json.load(file)

    ids = []
    for item in file_contents:
        ids.append(item['id'])
    
    get_contents_response = metaphor.get_contents(ids)

    output_data = []

    for item in get_contents_response.contents:
        content_dict = {}
        content_dict['ID'] = item.id
        content_dict['URL'] = item.url
        content_dict['Title'] = item.title

        content_dict['Extract'] = html_parser.remove_tags(item.extract)

        output_data.append(content_dict)

    with open(output_json_file, 'w') as file:
        json.dump(output_data, file)

# Usage example:

