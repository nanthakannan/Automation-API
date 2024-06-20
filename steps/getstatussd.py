import requests
import json
from behave import given, then
from utils.utils import convert_to_int
from responses.response import save_response
from methods.common_methods import send_get_url_request
from environment import LAST_RESPONSE_FILE_PATH
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@given('I send a GET request to the endpoint "{url}"')
def send_get_request(context, url):
    print ("URL is :" + url)
    logging.info("URL : " + url)
    full_url = context.base_url+url
    logging.info("baseURL is : " + full_url)
    response = send_get_url_request(full_url)
     # Print the status code
    logging.info(f"Status code: {response.status_code}")
    save_response(response, LAST_RESPONSE_FILE_PATH)
   
   
@then(u'the response status code should be "200"')
def step_impl(context):
    pass


@then(u'kill the request')
def step_impl1(context):
   pass