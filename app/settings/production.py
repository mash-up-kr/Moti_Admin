from .base import *

from pathlib import Path
env_path = Path('.') / '.env.production'
load_dotenv(dotenv_path=env_path)

SECRET_KEY = os.environ.get('SECRET_KEY', 'SOME+RANDOM+KEY(z9+3vnm(jb0u@&w68t#5_e8s9-lbfhv-')

ALLOWED_HOSTS = ["*"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

INTERNAL_IPS = ["*"]
ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_NAME'),
        'USER': os.getenv('MYSQL_USER'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': os.getenv('MYSQL_HOST'),
        'PORT': os.getenv('MYSQL_PORT'),
    }
}