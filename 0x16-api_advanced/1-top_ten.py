#!/usr/bin/python3
""" requests subs """
import requests


def top_ten(subreddit):
    """ number of subscribers"""
    base_url = 'https://www.reddit.com/r/{}/hot.json?limit=2'.format(subreddit)
    headers = {'User-Agent': 'alx_agent'}
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        print(response.json()["data"]['children'])
    else:
        return 0
