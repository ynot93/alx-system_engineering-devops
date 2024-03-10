#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles
of all hot articles and prints a sorted count of given keywords.
"""

import re
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Find hot articles of a subreddit."""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyUserAgent"}
    params = {"after": after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])
        hot_list += [post["data"]["title"] for post in children]
        after = data.get("after")

        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, after)

    except requests.exceptions.RequestException:
        return hot_list


def count_words(subreddit, word_list):
    """Prints sorted count of keywords."""
    hot_list = recurse(subreddit)
    if hot_list is None:
        hot_list = []
    if word_list is None:
        word_list = []
    results = {}

    for word in word_list:
        count = 0
        word_pattern = r"\b{}\b".format(word)
        for title in hot_list:
            count += len(re.findall(word_pattern, title, re.I))

        results[word.lower()] = results.get(word.lower(), 0) + count

    results = sorted(results.items(), key=lambda item: (
        item[1], item[0]), reverse=True)
    for word, count in results:
        if count:
            print(f"{word}: {count}")
