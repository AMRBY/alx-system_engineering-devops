#!/usr/bin/python3
""" requests subs """
import requests


def number_of_subscribers(subreddit):
    """ number of subscribers"""
    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'alx_agent'}
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json()["data"]["subscribers"])
    else:
        return 0
