from ariadne import QueryType, MutationType
from gameAnalytics.models import User
from gameAnalytics.errors.custom import UserInputError
import jwt
import datetime

query = QueryType()
mutation = MutationType()


@mutation.field("logIn")
def resolve_logIn(_, info, username, password):
    user = User.objects.get(username=username)
    if user.password == password:
        expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=12)
        token = jwt.encode({'id':user.id, 'exp': expiration}, "secret")
        print(token)
        return user
    else:
        raise UserInputError('User/Password incorrect.')


resolvers = [query, mutation]