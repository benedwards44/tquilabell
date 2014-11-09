# tquilabell
Application that subscribes to a Salesforce streaming API and rings a bell!

To run from a Python shell:
'''
from topic_subscription import subscribe_to_topic
sandbox = False
api_version = 32
subscribe_to_topic(sandbox, api_version)
'''
