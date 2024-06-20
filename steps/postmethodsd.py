import requests
import logging
import json
from behave import given, when, then
from methods.common_methods import send_post_request, generate_headers, generate_post_body
from responses.response import save_response
from environment import LAST_RESPONSE_FILE_PATH



@given('User navigates to "{URL}"')
def user_nav_to_url(context, URL):
    context.full_url = context.base_url+URL
    logging.info("Response URL:" + context.full_url)

@given('user enters with "{name}" and "{job}"')
def user_enters_details(context, name, job):
    context.name = name
    context.job = job

@when('user submits the request')
def send_post_Method(context):
    # full_url = context.base_url + "/api/users"
    logging.info("Response URL1:" + context.full_url)
    body = generate_post_body(context.name, context.job)  # Generate the JSON body
    headers = generate_headers()  # Generate the request headers
    context.response = requests.post(context.full_url, json=body, headers=headers)
    response_data = json.loads(context.response.text)
    response_name = response_data.get("name")
    logging.info("Name from the response:" + response_name)
    try:
     assert response_name == context.name, f"Expected name: {context.name}, Actual name: {response_name}"
     #assert response_name == "tester", f"Expected name: {"tester"}, Actual name: {response_name}"
    except json.JSONDecodeError as e:
        assert False, f"Failed to parse JSON response: {e}"
    except KeyError as e:
        assert False, f"Response does not contain 'name' attribute: {e}"
    
    # Save the response to a file if needed
    if context.response.status_code == 201:
        save_response(context.response, LAST_RESPONSE_FILE_PATH)
    
    # context.response = send_post_request(context.base_url, context.name, context.job, LAST_RESPONSE_FILE_PATH)

@then('status should be "{status}"')
def verify_status(context, status):
    expected_status = int(status)
    assert context.response.status_code == expected_status, f"Expected status: {expected_status}, Actual status: {context.response.status_code}"
