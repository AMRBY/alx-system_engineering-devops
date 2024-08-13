#!/usr/bin/python3
""" requests subs """
import requests


def top_ten(subreddit):
    """Top ten hot posts"""
    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'amrby'}
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        lista = response.json()["data"]['children']
        for i in lista[:10]:
            print(f">>>{i['data']['title']}")
    else:
        return 0
