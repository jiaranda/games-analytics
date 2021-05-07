from ariadne import QueryType, MutationType
from gameAnalytics.models import User
from gameAnalytics.errors.custom import UserInputError

query = QueryType()
mutation = MutationType()


@query.field("getUsers")
def resolve_getUsers(_, info):
    return User.objects.all()


@query.field("getUser")
def resolve_getUser(_, info, id):
    user = User.objects.get(id=id)
    return user


@mutation.field("createUser")
def resolve_createUser(_, info, username, password, email):
    user = User(
        username=username, password=password, email=email
    )
    user.full_clean()
    user.save()
    return user


@mutation.field("updateUser")
def resolve_updateUser(_, info, id, password=None, username=None):
    user = User.objects.get(id=id)
    if password is not None:
        user.password = password
    if username is not None:
        user.username = username
    user.full_clean()
    user.save()
    return user


@mutation.field("deleteUser")
def resolve_deleteUser(_, info, id):
    user = User.objects.get(id=id)
    user.delete()
    return True


resolvers = [query, mutation]
