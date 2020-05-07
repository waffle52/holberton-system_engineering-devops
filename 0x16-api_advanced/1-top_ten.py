#!/usr/bin/python3
""" Queries the reddit API for titles of the top ten hot posts """
import json
import requests


def top_ten(subreddit):
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {'User-Agent': 'My User Agent 1.0'}
        sub_red = requests.get(url, headers=headers, allow_redirects=False)
        data = sub_red.json()
        for x in range(0, 10):
            print(data['data']['children'][x]['data']['title'])
    except:
        print(None)
