import requests
import logging
import json
from behave import given, when, then
from methods.common_methods import send_delete_request
from responses.response import save_response
from environment import LAST_RESPONSE_FILE_PATH

@given('User navigates to delete "{URL}"')
def user_nav_to_url(context, URL):
    context.full_url = context.delete_url+URL
    logging.info("Response URL:" + context.full_url)


@when(u'user submits the delete request')
def send_delete_request_method(context):
    logging.info("Response URL1:" + context.full_url)
    # Assuming context.delete_url is set appropriately before this step
    context.response = send_delete_request(context.delete_url)
    # response_data = json.loads(context.response.text)
    logging.info(context.response)
        # Save the response to a file if needed
    # if context.response.status_code == 200:
    #     save_response(context.response, LAST_RESPONSE_FILE_PATH)