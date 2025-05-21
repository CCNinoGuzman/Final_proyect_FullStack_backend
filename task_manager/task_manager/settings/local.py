from .base import *
from dotenv import load_dotenv
import os 


dot_env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dot_env_path)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
<<<<<<< Updated upstream
        "NAME": BASE_DIR / "db.sqlite3",
=======
        "NAME": os.getenv("DARABASE_NAME"),
        'USER': os.getenv("DATABASE_USER"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),
        'HOST': os.getenv("DATABASE_HOST"),
        'PORT': os.getenv("DATABASE_PORT"),

>>>>>>> Stashed changes
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"
