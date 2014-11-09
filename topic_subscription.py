from login import login
from client import Client
from bayeux.bayeux_client import BayeuxClient
import json

def subscribe_to_topic(sandbox, api_version):

	# Login to Salesforce to retrieve token and other variables
	connection = login(sandbox)

	bc = BayeuxClient(str(connection.instance_url) + '/cometd/' + str(api_version) + '.0/', str(connection.access_token))
	bc.register('/topic/ClosedWonOpportunities', topic_callback)
	bc.start()

def topic_callback(data):
	print data
