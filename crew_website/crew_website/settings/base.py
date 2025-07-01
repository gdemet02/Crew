import os
from pathlib import Path

# BASE & PROJECT directories
BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_DIR = BASE_DIR / "crew_website"

# Security
SECRET_KEY = "your-secret-key"  # Replace in production!
DEBUG = True
ALLOWED_HOSTS = []

# Environment flag
ENVIRONMENT = os.getenv("DJANGO_ENV", "development")

# Applications
INSTALLED_APPS = [
    "home",
    "search",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django_filters",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "crew_website.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            PROJECT_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'crew_website.context_processors.global_components',
            ],
        },
    },
]

WSGI_APPLICATION = "crew_website.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crewdb',
        'USER': 'crewuser',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Language and time zone
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files setup
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    PROJECT_DIR / "static",  # Place your html assets in this folder
]
STATIC_ROOT = BASE_DIR / "staticfiles"  # Only used in production when collectstatic is run

# Media files (user uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Static storage backends depending on environment
if ENVIRONMENT == "production":
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
        },
    }
else:
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Upload field support
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

# Wagtail site name
WAGTAIL_SITE_NAME = "crew_website"

# Search backend
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL for Wagtail admin (optional)
WAGTAILADMIN_BASE_URL = "http://localhost:8000"

# Allowed document types (optional)
WAGTAILDOCS_EXTENSIONS = [
    "csv", "docx", "key", "odt", "pdf", "pptx", "rtf", "txt", "xlsx", "zip",
]
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "your.smtp.host"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "you@domain.com"
EMAIL_HOST_PASSWORD = "yourpassword"
DEFAULT_FROM_EMAIL = "you@domain.com"
