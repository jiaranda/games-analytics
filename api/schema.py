from ariadne import QueryType, make_executable_schema, load_schema_from_path

type_defs = load_schema_from_path("api/types")
schema = make_executable_schema(type_defs)