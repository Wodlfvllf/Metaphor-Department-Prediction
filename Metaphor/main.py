import json
import Departments_classification
import get_relevant_urls
import json
# from metaphor_utils import search_metaphor, save_results_to_json
import get_content_from_url
# Your API key
api_key = 'f4c68fbc-bcbc-4a85-b3f3-8d591adf0020'

def save_results_to_json(results, output_file):
    with open(output_file, 'w') as file:
        json.dump(results, file)

def perform_search_and_save(query, output_file, num_results=10):
    relevant_urls = get_relevant_urls.search_metaphor(query, num_results=num_results)
    save_results_to_json(relevant_urls, output_file)

# Define your queries and output file paths
english_query = 'Here are recent news articles from hindustan times and economic times mentioning Indian government department and ministry'
english_output_file = 'english_relevant_urls_id.json'

hindi_query = 'Here are recent hindi news articles from regional hindi newspapers mentioning Indian government department and ministry'
hindi_output_file = 'hindi_relevant_urls_id.json'

# Perform the searches and save results
perform_search_and_save(english_query, english_output_file)
perform_search_and_save(hindi_query, hindi_output_file)

val = input("Enter the Language...")
if val == "Hindi":
    input_json_file = hindi_output_file
    output_json_file = 'content.json'
    get_content_from_url.retrieve_and_save_contents(input_json_file, output_json_file, language = "English")
else:
    input_json_file = english_output_file
    output_json_file = 'content.json'
    get_content_from_url.retrieve_and_save_contents(input_json_file, output_json_file, language = "Hindi")

with open('content.json', 'r') as file:
    data = json.load(file)

items = data[0]
extract = items['Extract']
# print(extract[:10])
ob = Departments_classification.Department_classifier()
options = ob.main('Inference', extract)
print(options)
