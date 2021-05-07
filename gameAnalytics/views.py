from django.http import JsonResponse


def index(request):
    return JsonResponse({"message": "Hello World! Go to /gameAnalytics/graphql"})
