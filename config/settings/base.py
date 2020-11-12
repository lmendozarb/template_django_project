"""
Django settings for ecommerce project.

Django 2.2.14.

Base settings to build ither settings files upon.
"""

import os
import environ


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path("apps")

env = environ.Env()

# Base
DEBUG = env.bool("DJANGO_DEBUG", False)

# Language and timezone
TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-pe"
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# DATABASES
DATABASES = {
    "default": env.db("DATABASE_URL"),
}
# DATABASES['default']['ATOMIC_REQUESTS'] = True

# URLs
ROOT_URLCONF = "config.urls"

# WSGI
WSGI_APPLICATION = "config.wsgi.application"

# Apps
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = []

LOCAL_APPS = []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Passwords
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Middlewares
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Static files
STATIC_URL = "/static/"
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Media
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            ],
        },
    },
]
# Security
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# Email
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)

# Admin
ADMIN_URL = "admin/"
ADMINS = [
    ("""Luis Mendoza""", "lmendoza@hacklibre.com"),
]
MANAGERS = ADMINS

# Celery
INSTALLED_APPS += ["apps.taskapp.celery.CeleryAppConfig"]
if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERYD_TASK_TIME_LIMIT = 5 * 60
CELERYD_TASK_SOFT_TIME_LIMIT = 60

# Others
PHONENUMBER_DB_FORMAT = "NATIONAL"
PHONENUMBER_DEFAULT_REGION = "PE"
