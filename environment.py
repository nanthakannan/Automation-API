# from responses.response import save_response
import configparser
import logging




# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables from .env file
# load_dotenv()

config = configparser.ConfigParser()
config.read('.env')

#BaseURL
base_url = config['MyData']['base_url']
logging.info("url for mentioned is : " + base_url)

#DeleteURL
delete_url = config['MyData']['delete_url']
logging.info("Delete URL is : " + delete_url)



# Define file paths as constants or environment variables
LAST_RESPONSE_FILE_PATH = "D://API-Automation_Framework//responses//last_response.json"



def before_all(context):
    

    # Load base URL from environment variables
    context.base_url = base_url
    context.delete_url = delete_url

    # # Load auth token from response file
    # auth_token_file = 'responses/auth_token.json'
    # auth_token_response = save_response(auth_token_file)
    # context.auth_token = auth_token_response.get('auth_token')
    
    
#    # Save the response
#     if hasattr(context, 'response'):
#         save_response(context.response, LAST_RESPONSE_FILE_PATH)

    # Other environment setup tasks if needed
