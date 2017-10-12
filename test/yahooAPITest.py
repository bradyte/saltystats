from requests_oauthlib import OAuth1Session
#import requests
#from requests_oauthlib import OAuth1

#put your keys in a file where line 1 is your client key and line 2 
#is your client secret
file = open('yahooKeys.txt','r')
keys = file.read().splitlines()

client_key      = keys[0]
client_secret   = keys[1]

#Yahoo API URLs
request_token_url = 'https://api.login.yahoo.com/oauth/v2/get_request_token'
base_authorization_url = 'https://api.login.yahoo.com/oauth/v2/request_auth'
access_token_url = 'https://api.login.yahoo.com/oauth/v2/get_token'

#Obtain a request token which will identify you (the client) in the next step.
oauth = OAuth1Session(client_key, client_secret=client_secret)
fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

#Obtain authorization from the user (resource owner) to access their protected 
#resources (images, tweets, etc.). 
if 0: 
    authorization_url = oauth.authorization_url(base_authorization_url)
    print('Please go here and authorize,', authorization_url)
    redirect_response = input('Paste the full redirect URL here: ')
    oauth_response = oauth.parse_authorization_response(redirect_response)
    verifier = oauth_response.get('oauth_verifier')
    
    #Obtain an access token from the OAuth provider.
    #Save this token as it can be re-used later.
    oauth = OAuth1Session(client_key,
                              client_secret=client_secret,
                              resource_owner_key=resource_owner_key,
                              resource_owner_secret=resource_owner_secret,
                              verifier=verifier)
    oauth_tokens = oauth.fetch_access_token(access_token_url)
    
    resource_owner_key = fetch_response.get('oauth_token')
    resource_owner_secret = fetch_response.get('oauth_token_secret')
#Once you have access, it is open for 60 minutes
#The if 0 statement is to not have to verify every time.

#Access protected resources. OAuth1 access tokens typically do not
#expire and may be re-used until revoked by the user or yourself.
protected_url = 'http://fantasysports.yahooapis.com/fantasy/v2/leagues;league_keys=371.l.470610'
oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

r = oauth.get(protected_url)

print (r)







