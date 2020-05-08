#!/usr/bin/python3
""" recursive function that queries Reddit API and
returns list containing the titles of all hot articles
"""
import json
import requests


def recurse(subreddit, hot_list=[], x=0, after=''):
    try:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
        headers = {'User-Agent': 'My User Agent 1.0'}
        sub_red = requests.get(url, headers=headers, allow_redirects=False)
        data = sub_red.json()
        length = len(data['data']['children'])

        if (x == length and data['data']['after'] is None):
            return (hot_list)
        elif(x == length):
            x = 0
            after = data['data']['after']
            return (recurse(subreddit, hot_list, x, after))
        else:
            hot_list.append(data['data']['children'][x]['data']['title'])
            x += 1
            return (recurse(subreddit, hot_list, x, after))
    except Exception as E:
        print("Error: {}".format(E))
        return (None)
