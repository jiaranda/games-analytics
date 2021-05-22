from ariadne import QueryType, MutationType
from gameAnalytics.models import Player
from gameAnalytics.errors.custom import PlayerInputError

query = QueryType()
mutation = MutationType()


@query.field("getPlayers")
def resolve_getPlayers(_, info):
    return Player.objects.all()


@query.field("getPlayer")
def resolve_getPlayer(_, info, id):
    player = Player.objects.get(id=id)
    return player


@mutation.field("createPlayer")
def resolve_createPlayer(_, info, name):
    player = Player(
        name=name
    )
    player.full_clean()
    player.save()
    return player


@mutation.field("updatePlayer")
def resolve_updatePlayer(_, info, id, name=None):
    player = Player.objects.get(id=id)
    if name is not None:
        player.name = name
    player.full_clean()
    player.save()
    return player


@mutation.field("deletePlayer")
def resolve_deletePlayer(_, info, id):
    player = player.objects.get(id=id)
    player.delete()
    return True


resolvers = [query, mutation]
