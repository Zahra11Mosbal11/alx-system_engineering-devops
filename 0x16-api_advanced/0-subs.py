#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscriber
"""
import requests


def number_of_subscribers(subreddit):
    """ Construct the URL for the subreddit's about page in JSON format"""
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers={'User-Agent': 'app/1.0'})
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
