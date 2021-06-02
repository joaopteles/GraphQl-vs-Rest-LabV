import app.getRepo.query_utils as query_utils
import requests

# payload = '{"ticket":{"requester":{"name":"Dan Pawluk", "email":"daniel.pawluk@me.com"}, "subject":"My printer is on fire!", "comment": { "body": "I want thousands of tickets" }}}'


def executeQuery():
    s = requests.Session()
    s.headers.update({'Content-Type': 'application/json'})
    s.headers.update({'Accept': 'application/vnd.github.v3+json'})
    s.headers.update(
        {"Authorization": "token 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"})

    try:
        r = s.get(
            "https://api.github.com/search/repositories?q=stars:>100+language:JavaScript")
        # print("finished with request number:" + str(x))
        return r
    except requests.exceptions.ConnectionError as e:
        print("There was a connection error: %s" % (e))
    except requests.exceptions.Timeout as e:
        print("There was a timeout!!!")


query_template = """

"""


def parse_data(res):
    repositories = res['data']['search']['nodes']
    page_info = res['data']['search']['pageInfo']
    rate_limit = res['data']['rateLimit']
    return {"repositories": repositories, "page_info": page_info, "rate_limit": rate_limit}


def get_repositories(first, after):
    query = query_utils.criar_query(
        {"$after": after, "$first": first}, query_template)
    data = query_utils.execute_query(query)
    return parse_data(data)
