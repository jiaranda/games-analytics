from gameAnalytics.models import Users

def resolve_getUsers(_, info):
    return {
        "username": User.username,
        "email": User.email
    }

def create_user(_, username, password, email):
    return {'True': True}
    # user = User.objects.create(info)
    # return {'username': user.username, 'email' : user.email}