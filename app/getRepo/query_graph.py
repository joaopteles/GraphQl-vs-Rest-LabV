import app.getRepo.query_utils as query_utils

query_template = """{
  search(query: ReplaceQuery, type: REPOSITORY, first: 1) {
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


def get_repository(query):
    data = query_utils.execute_query(
        query_template.replace("ReplaceQuery", query))
    return data
