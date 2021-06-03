import requests
import utils

query_template = """{
  search(query: "$query", type: REPOSITORY, first: $first) {
    nodes {
      ... on Repository {
        id
        name
        url
        owner {
          login
        }
      }
    }
  }
}"""


def execute_query(params, item):
    query = mount_query(params, item)
    res = requests.post("https://api.github.com/graphql", json={'query': query}, headers={
        'Content-Type': 'application/json',
        'Authorization': 'bearer {}'.format(utils.token)
    })
    return res, len(query)


def mount_query(q, i):
    return query_template.replace("$first", str(i)).replace("$query", q)
