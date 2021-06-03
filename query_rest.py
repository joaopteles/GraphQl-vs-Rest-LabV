import requests
import utils


def execute_query(query, item):
    params = "q={}&per_page={}".format(query, item)
    res = requests.get("https://api.github.com/search/repositories?{}".format(params), headers={
        'Content-Type': 'application/json',
        'Authorization': 'bearer {}'.format(utils.token)
    })
    return res, len(params)
