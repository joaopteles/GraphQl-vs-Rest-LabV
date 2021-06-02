import app.getRepo.query_utils as query_utils

query_template = """{
  search(query: "stars:>100 language:JavaScript", type: REPOSITORY, first: 10) {
    nodes {
      ... on Repository {
        id
        name
        url
        owner {
          login
        }
        closed: pullRequests(states: CLOSED) {
          totalCount
        }
        merged: pullRequests(states: MERGED){
          totalCount
        }
      }
    }
  }
}"""


def parse_data(res):
    repositories = res['data']['search']['nodes']
    page_info = res['data']['search']['pageInfo']
    rate_limit = res['data']['rateLimit']
    return {"repositories": repositories, "page_info": page_info, "rate_limit": rate_limit}


def get_repository():
    data = query_utils.execute_query(query_template)
    return data
