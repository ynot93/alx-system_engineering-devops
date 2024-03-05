#!/usr/bin/python3
"""
Use recursion to fetch hot posts from reddit

"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 100, 'after': after}
    headers = {"User-Agent": "MyRedditApp/1.0"}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']

        for post in posts:
            hot_list.append(post['data']['title'])

        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
