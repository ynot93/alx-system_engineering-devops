#!/usr/bin/python3
"""
Returns total number of subscribers for a subreddit.
Return 0 if invalid subreddit is given.

"""
import requests


def number_of_subscribers(subreddit):
    """get total number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'User-Agent': 'TonyMputhia (by /u/Y_Not93)'}

    response = requests.get(url, headers=headers)
    print(response.text)

    if response.status_code == 200:
        data = response.json()
        subscribers = ['data']['subscribers']
        return subscribers
    else:
        return 0
