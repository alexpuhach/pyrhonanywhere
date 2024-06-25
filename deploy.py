import requests
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('USERNAME')
token = os.getenv('TOKEN')
domain_name = os.getenv('DOMAIN_NAME')

response = requests.post(
    f'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/',
    headers={'Authorization': f'Token {token}'}
)

if response.status_code == 200:
    print('Reload successful')
else:
    print('Failed to reload')

