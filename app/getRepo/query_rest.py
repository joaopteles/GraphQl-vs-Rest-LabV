import app.getRepo.query_utils as query_utils
import requests


def executeQuery(query):
    s = requests.Session()
    s.headers.update({'Content-Type': 'application/json'})
    s.headers.update({'Accept': 'application/vnd.github.v3+json'})
    s.headers.update(
        {"Authorization": "{token}"})
    url = "https://api.github.com/search/repositories?queryReplace".replace(
        query, "queryReplace")

    try:
        r = s.get(url)
        return r
    except requests.exceptions.ConnectionError as e:
        print("There was a connection error: %s" % (e))
    except requests.exceptions.Timeout as e:
        print("There was a timeout!!!")
