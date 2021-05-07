from ariadne import QueryType, make_executable_schema, load_schema_from_path, MutationType

from .resolvers import resolvers


type_defs = load_schema_from_path("gameAnalytics/graphql/types")
schema = make_executable_schema(type_defs, resolvers)
