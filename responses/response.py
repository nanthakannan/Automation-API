import json
import logging
# from methods.common_methods import send_api_request



# Configure logging
logging.basicConfig(level=logging.DEBUG)

def save_response(response, file_path):
    """
    Save the response content to a JSON file.

    Args:
        response (Response): The response object.
        file_path (str): Path to save the JSON file.
    """
    # Check if the response content is empty
    if response.content:
        try:
            # Decode the response content as JSON and save it to the file
            with open(file_path, 'w') as file:
                json.dump(response.json(), file)
        except json.JSONDecodeError as e:
            # Log the error if JSON decoding fails
            logging.info(f"Error decoding JSON: {e}")
    else:
        # Log a message if the response content is empty
        logging.info("Response content is empty, cannot save to JSON file.")
        
        
# def save_responses_to_file():
#     responses = []
#     urls = {
#         'GET': 'https://example.com/get_endpoint',
#         'POST': 'https://example.com/post_endpoint',
#         'DELETE': 'https://example.com/delete_endpoint',
#         'PUT': 'https://example.com/put_endpoint'
#     }
#     post_data = {'key': 'value'}
#     for method, url in urls.items():
#         response = send_api_request(method, url, data=post_data if method in ['POST', 'PUT'] else None)
#         if response:
#             responses.append({'method': method, 'url': url, 'status_code': response.status_code, 'content': response.json()})
#     with open('responses.json', 'w') as f:
#         json.dump(responses, f, indent=4)

# # Call the function if the script is run directly
# if __name__ == "__main__":
#     save_responses_to_file()
