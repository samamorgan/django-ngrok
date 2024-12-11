from pathlib import Path

from django.utils.crypto import get_random_string

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = get_random_string(50)
DEBUG = True
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = ["django_ngrok"]
ROOT_URLCONF = "tests.urls"
