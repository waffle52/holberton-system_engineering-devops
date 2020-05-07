#!/usr/bin/python3
""" Queries the reddit API for subscriber count for a passed subreddit"""
import json
import requests


def number_of_subscribers(subreddit):
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {'User-Agent': 'My User Agent 1.0'}
        sub_red = requests.get(url, headers=headers, allow_redirects=False)
        data = sub_red.json()
        return (data['data']['subscribers'])
    except:
        return (0)
