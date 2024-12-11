import os
from dotenv import load_dotenv, dotenv_values
from ebics_api_client import ebics_api_client

load_dotenv()

client = ebics_api_client.EbicsApiClient(os.getenv('API_KEY'), os.getenv('API_HOST'))

connection = client.connection_create({
  'host_url': os.getenv('HOST_URL'),
  'host_id': os.getenv('HOST_ID'),
  'partner_id': os.getenv('PARTNER_ID'),
  'user_id': os.getenv('USER_ID'),
  'keyring_op': 'NOT_STORE',
  'name': 'My Connection',
})

print(connection)

connection = client.connection_get('1')

print(connection)