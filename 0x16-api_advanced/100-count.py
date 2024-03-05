#!/usr/bin/python3
"""
Prints a sorted count of given keywords from title of
hot articles

"""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    if word_count is None:
        word_count = {}

    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}"
        .format(subreddit, after)

    headers = {"User-Agent": "MyRedditApp/1.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Invalid subreddit or unable to fetch data.")
        return

    data = response.json()
    posts = data['data']['children']
    after = data['data']['after']

    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            if word.lower() in title:
                if word.lower() in word_count:
                    word_count[word.lower()] += 1
                else:
                    word_count[word.lower()] = 1

    if after is not None:
        return count_words(subreddit, word_list, after, word_count)
    else:
        sorted_word_count = sorted(
                word_count.items(), key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_word_count:
            print("{}: {}".format(word, count))
