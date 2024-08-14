#!/usr/bin/python3
"""
Recursive function to query the Reddit API
and return a list of hot article titles
for a given subreddit.

"""
import requests


def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "MyBot/1.0"}

    response = requests.get(url, headers=headers)
    data = response.json()
    posts = data['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])

    if 'after' in data['data'] and data['data']['after'] is not None:
        new_url = url + f"&after={data['data']['after']}"
        recurse(subreddit, hot_list)
    else:
        return None
    return hot_list


if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")
    result = recurse(subreddit)
    if result is not None:
        print(len(result))
    else:
        print("None")
