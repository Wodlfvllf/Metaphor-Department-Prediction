from metaphor_python import Metaphor
from datetime import date, timedelta
import json

def search_metaphor(query, num_results=10):
    # Your API key
    api_key = 'f4c68fbc-bcbc-4a85-b3f3-8d591adf0020'
    
    # Initialize Metaphor API
    metaphor = Metaphor(api_key)

    # Date range for search
    end_date = date.today()
    start_date = end_date - timedelta(days=30)

    # Format the date range in ISO 8601 format
    start_date_str = start_date.isoformat()
    end_date_str = end_date.isoformat()

    # Perform the search
    search_response = metaphor.search(
        query,
        num_results=num_results,
        use_autoprompt=True,
        start_published_date=start_date_str,
        end_published_date=end_date_str
    )

    # Extract relevant URLs and their IDs
    relevant_urls_id = [{"url": result.url, "id": result.id} for result in search_response.results]

    return relevant_urls_id


