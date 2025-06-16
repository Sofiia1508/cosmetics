# DjangoProject1/settings.py

import os # <--- ОБОВ'ЯЗКОВО! ДОДАЙТЕ ЦЕЙ РЯДОК НА САМОМУ ПОЧАТКУ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # <--- ОБОВ'ЯЗКОВО! ДОДАЙТЕ ЦЕЙ РЯДОК


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ваша_секретна_фраза_тут' # Залиште свою або згенеруйте нову

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # <--- ПЕРЕВІРТЕ, ЩО ЦЕ TRUE ДЛЯ РОЗРОБКИ.

ALLOWED_HOSTS = ['127.0.0.1', 'localhost'] # <--- ОБОВ'ЯЗКОВО! ДОДАЙТЕ ЦЕЙ РЯДОК АБО ВИПРАВТЕ.


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cosmetics', # <--- ПЕРЕВІРТЕ НАЯВНІСТЬ 'cosmetics'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoProject1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Цей шлях для загальних шаблонів проекту (можна залишити)
        'APP_DIRS': True, # <--- ПЕРЕВІРТЕ: МАЄ БУТИ True. Це дозволяє Django шукати шаблони в папках 'templates' додатків.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoProject1.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
LANGUAGE_CODE = 'uk' # Можна змінити на 'uk'

TIME_ZONE = 'Europe/Kiev' # Можна змінити на свій часовий пояс

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), # <--- ПЕРЕВІРТЕ НАЯВНІСТЬ ЦЬОГО РЯДКА. Це вказує на кореневу папку static.
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # <--- ПЕРЕВІРТЕ НАЯВНІСТЬ ЦЬОГО РЯДКА (для розгортання)

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'