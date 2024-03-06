#!/usr/bin/python3
"""
Print title of first 10 hot posts

"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyRedditApp/1.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                print(post['data']['title'])
        else:
            print("No posts found in the subreddit.")
    else:
        print("Invalid subreddit or unable to fetch data.")
