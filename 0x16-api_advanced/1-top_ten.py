#!/usr/bin/python3
"""
Queries the Reddit API and prints the
titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyBot/1.0"}  # Set custom User-Agent

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print("None")


if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")
    top_ten(subreddit)
