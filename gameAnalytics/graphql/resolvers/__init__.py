from .users import resolvers as users_resolvers
from .players import resolvers as players_resolvers

resolvers = [*users_resolvers,
     *players_resolvers]
