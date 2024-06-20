import requests
import json
import logging
# from environment import save_response

from responses.response import save_response

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def send_get_url_request(get_url):
    """
    Sends a GET request to the specified URL and returns the response.
    
    Args:
        full_url (str): The full URL to send the GET request to.

    Returns:
        Response: The response object.
    """
    
    headers = {
        'Accept': 'application/json',  # Specify the content type(s) the client can accept
        'User-Agent': 'YourUserAgent/1.0'  # Optional: Include a user-agent header
    }
    
    response = requests.get(get_url, headers=headers)
    return response



def generate_post_body(name, job):
    """
    Generate the JSON body for a POST request.

    Args:
        name (str): The name value.
        job (str): The job value.

    Returns:
        dict: The JSON body.
    """
    body = {
        "name": name,
        "job": job
    }
    return body

def generate_headers(content_type='application/json'):
    """
    Generate the request headers.

    Args:
        content_type (str): The content type of the request.

    Returns:
        dict: The request headers.
    """
    headers = {
        'Content-Type': content_type
    }
    return headers

def send_post_request(full_url, name, job, file_path):
    
    logging.info ("Details are : " + full_url, name, job, file_path)
    """
    Send a POST request to the specified endpoint.

    Args:
        base_url (str): The base URL of the API.
        url (str): The endpoint URL.
        name (str): The name value.
        job (str): The job value.
        file_path (str): The file path to save the response.

    Returns:
        Response: The response object.
    """
    try:
        body = generate_post_body(name, job)  # Generate the JSON body
        headers = generate_headers()  # Generate the request headers
        response = requests.post(full_url, json=body, headers=headers)

        # Log the response status code and content
        logging.info(f"Response status code: {response.status_code}")
        logging.info(f"Response content: {response.text}")

        # Save the response to a file if needed
        if response.status_code == 201:
            save_response(response, file_path)        
        return response, response.text

    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        raise e
    

def send_api_request(method, url, data=None):
    response = None
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, json=data)
    elif method == 'DELETE':
        response = requests.delete(url)
    elif method == 'PUT':
        response = requests.put(url, json=data)
    return response


def send_put_request(full_url, name, job, file_path):
    """
    Send a PUT request to the specified endpoint.

    Args:
        full_url (str): The full URL of the endpoint.
        name (str): The name value.
        job (str): The job value.
        file_path (str): The file path to save the response.

    Returns:
        Response: The response object.
    """
    try:
        body = generate_post_body(name, job)  # Generate the JSON body
        headers = generate_headers()  # Generate the request headers
        response = requests.put(full_url, json=body, headers=headers)

        # Log the response status code and content
        logging.info(f"Response status code: {response.status_code}")
        logging.info(f"Response content: {response.text}")

        # Save the response to a file if needed
        if response.status_code == 200:  # Adjust status code as per your API
            save_response(response, file_path)        
        return response

    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        raise e

def send_delete_request(full_url):
    """
    Send a DELETE request to the specified endpoint.

    Args:
        full_url (str): The full URL of the endpoint.
        file_path (str, optional): The file path to save the response. Defaults to None.

    Returns:
        Response: The response object.
    """
    try:
        headers = generate_headers()  # Generate the request headers
        response = requests.delete(full_url)

        # Log the response status code and content
        logging.info(f"Response status code: {response.status_code}")
        logging.info(f"Response content: {response.text}")

        # Save the response to a file if needed
        if response.status_code == 200:  # Adjust status code as per your API
            save_response(response)
        
        return response

    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        raise e

