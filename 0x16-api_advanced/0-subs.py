#!/usr/bin/python3
""" requests subs """
import requests

#if __name__ == "__main__":
#def number_of_subscribers(subreddit):
#    """return number of subscribers"""
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': 'Tiny_Palpitation_259', 'password': 'Amoura1989#?!'}
auth = requests.auth.HTTPBasicAuth('3BjPKYm4CkLn8X7O9TfHUw', 'Y4P65CwDIPj8CbEKSILlKmexIUrs7w')
r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'alx_agent'},
		  auth=auth)
d = r.json()
token = 'bearer ' + d['access_token']

base_url = 'https://oauth.reddit.com'

headers = {'Authorization': token, 'User-Agent': 'alx_agent'}
response = requests.get(base_url + '/api/v1/me', headers=headers)

if response.status_code == 200:
    print(response.json()['name'], response.json()['comment_karma'])
#payload = {'q': 'puppies', 'limit': 5, 'sort': 'relevance'}
payload = {'limit': 5}
api_url = base_url
response = requests.get(api_url + '/subreddits/mine/subscriber', headers=headers, params=payload)
print(response.status_code)
values = response.json()
print(response.text)
