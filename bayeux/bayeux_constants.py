HANDSHAKE_CHANNEL = '/meta/handshake'
CONNECT_CHANNEL = '/meta/connect'
DISCONNECT_CHANNEL = '/meta/disconnect'
SUBSCRIBE_CHANNEL = '/meta/subscribe'
UNSUBSCRIBE_CHANNEL = '/meta/unsubscribe'

# Use to enable debug logging into debug.log
ENABLE_DEBUG = True

HANDSHAKE_RETRY_INTERVAL = 5 #Retry interval in seconds for handshake requests
CONNECT_FAILURE_THRESHOLD = 3 #Number of failed connect requests before reissuing handshakes