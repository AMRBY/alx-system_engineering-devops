#!/usr/bin/python3
""" requests subs """
import requests


def top_ten(subreddit):
    """Top ten hot posts"""
    base_url = 'https://www.reddit.com/r/{}/hot.json?limit=9'.format(subreddit)
    headers = {'user-agent': 'amrby'}
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        for i in response.json()["data"]['children']:
            print(f">>>{i['data']['title']}")
    else:
        return 0
