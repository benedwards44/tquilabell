import requests
import json
import config
from client import Client

# Login using REST API to obtain auth token
def login(sandbox):

	# Set data payload
	data = {
		'grant_type': 'password',
		'client_id': config.CLIENT_ID,
		'client_secret': config.CLIENT_SECRET,
		'username': config.USERNAME,
		'password': config.PASSWORD
	}

	# Set login url based on sandbox or production
	login_url = 'https://login.salesforce.com/services/oauth2/token'
	if sandbox:
		login_url = 'https://test.salesforce.com/services/oauth2/token'

	# Login using REST API
	r = requests.post(login_url, data=data)

	# Set values for later use
	client = Client(r.json()['instance_url'], r.json()['access_token'])
	return client