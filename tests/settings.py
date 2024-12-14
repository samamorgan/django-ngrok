import os

from django.http import JsonResponse
from django.urls import path
from django.utils.crypto import get_random_string

SECRET_KEY = get_random_string(50)
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ["django_ngrok"]
ROOT_URLCONF = __name__
USE_TZ = False

NGROK_CONFIG = {
    "authtoken_from_env": True,
    "domain": os.getenv("NGROK_DOMAIN"),
}


def index(request):
    ping = request.GET.get("ping")

    return JsonResponse({"pong": ping})


urlpatterns = [
    path("", index),
]
