from requests_oauthlib import OAuth1Session
import requests
from requests_oauthlib import OAuth1


client_secret =
client_key = 

request_token_url = 'https://api.login.yahoo.com/oauth/v2/get_request_token'
base_authorization_url = 'https://api.login.yahoo.com/oauth/v2/request_auth'
access_token_url = 'https://api.login.yahoo.com/oauth/v2/get_token'

oauth = OAuth1Session(client_key,client_secret=client_secret)

fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

#authorize_url = base_authorization_url + '?oauth_token='
#authorize_url = authorize_url + resource_owner_key
#print ('Please go here and authorize,', authorize_url)
#verifier = input('Please input the verifier')

oauth = OAuth1Session(client_key,
                   client_secret=client_secret,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

oauth_tokens = oauth.fetch_access_token(access_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

print(oauth_tokens)
protected_url = 'http://fantasysports.yahooapis.com/fantasy/v2/game/nfl?format=json'

oauth = OAuth1(client_key,
                   client_secret=client_secret,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

r = requests.get(url=protected_url, auth=oauth)

print (r.content)
