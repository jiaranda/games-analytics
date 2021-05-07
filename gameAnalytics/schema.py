from ariadne import QueryType, make_executable_schema, load_schema_from_path, MutationType

from .resolvers import users

query = QueryType()
query.set_field("getUsers", users.resolve_getUsers)

mutation = MutationType()
mutation.set_field("createUser", users.create_user)

type_defs = load_schema_from_path("gameAnalytics/types")
schema = make_executable_schema(type_defs)