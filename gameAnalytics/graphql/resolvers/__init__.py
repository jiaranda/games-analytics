from .users import resolvers as users_resolvers
from .session import resolvers as session_resolvers
from .players import resolvers as players_resolvers

resolvers = [*users_resolvers,
     *players_resolvers,
     *session_resolvers]
