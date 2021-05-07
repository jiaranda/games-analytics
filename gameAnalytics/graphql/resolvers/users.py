from ariadne import QueryType, MutationType

query = QueryType()
mutation = MutationType()


@query.field("getUsers")
def resolve_getUsers(_, info):
    return [{
        "username": "javier",
        "email": "javier@hola.com"
    }]


resolvers = [query, mutation]
