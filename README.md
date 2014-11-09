# tquilabell
Application that subscribes to a Salesforce streaming API and rings a bell!

## Setup

### Create Push Topic

You will first need to create a Salesforce Push Topic. You can do this by running the following Apex script in an Execute Anonymous window:
    
    PushTopic pushTopic = new PushTopic();
    pushTopic.Name = 'ClosedWonOpportunities';
    pushTopic.Query = 'SELECT Id, Name, Amount, OwnerId FROM Opportunity Where StageName = \'Closed Won\'';
    pushTopic.ApiVersion = 32.0;
    pushTopic.NotifyForOperationCreate = true;
    pushTopic.NotifyForOperationUpdate = true;
    pushTopic.NotifyForOperationUndelete = true;
    pushTopic.NotifyForOperationDelete = true;
    pushTopic.NotifyForFields = 'Referenced';
    insert pushTopic;
    
You can find more detail on the Salesforce Streaming API at http://www.salesforce.com/developer/docs/api_streaming/

### Run Python script

To run from a Python shell:

    from topic_subscription import subscribe_to_topic
    sandbox = False
    api_version = 32
    topic = 'ClosedWonOpportunities'
    subscribe_to_topic(sandbox, api_version, topic)

