#!/usr/bin/python3
"""
Recursive function to query the Reddit API, parse hot
article titles, and print counts of given keywords.

"""
import requests


def count_words(subreddit, word_list, counts=None):
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "MunBot/1.0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1
        if 'after' in data['data'] and data['data']['after'] is not None:
            new_url = url + f"&after={data['data']['after']}"
            count_words(subreddit, word_list, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("None")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programmin 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [word for word in sys.argv[2].split()]
        count_words(subreddit, word_list)
