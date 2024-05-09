#!/usr/bin/python3
"""
Module to query the Reddit API and retrieve the number of
subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    retrieves the number of subscribers for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    user_agent = {'User-Agent': 'CustomUserAgent'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = get(url, headers=user_agent, allow_redirects=False)
        response.raise_for_status()
        output = response.json()
        return output.get('data').get('subscribers')
    except requests.exceptions.HTTPError as http_err:
        return 0
