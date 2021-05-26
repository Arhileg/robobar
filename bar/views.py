from django.http import HttpResponse

def index(request):
    return HttpResponse("Наш робобар привентствует тебя странник.")
