"""
Django settings for cloudlink_devs project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os


from django.contrib import staticfiles

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*m@g&%(lwkd+z1ad@xikydcsh*1*l79$ps^td4h-x4u(@!(k(c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# cloudlink_devs/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your custom apps
    'services',
    'core',
    'chatbot',
    'client_portal',
    'portfolio',
    'blog',
    'quotes',
    'mpesa_api',
]
# M-Pesa API Configuration
MPESA_CONFIG = {
    'CONSUMER_KEY': '2wAKKr3EQVZCjoG64vGRxk6R7vkXZapUFNYcGQsbIAaMebSD',
    'CONSUMER_SECRET': 'LVRxnPGajFSxe3EOuss7XRthQoZQKG8UBeVpbcGwgNWsbvRY1HyY5aZYjxSHZ195',
    'SHORTCODE': '174379',  # Use the test shortcode provided by Safaricom
    'PASS_KEY': 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919',
    'CALLBACK_URL': 'https://082c-102-0-17-78.ngrok-free.app/mpesa/callback/',
    'INITIATOR_NAME': 'testapi',
    'SECURITY_CREDENTIAL': 'QdAeWL42MfpZgUfWiun8XJcAEg/UH+eTDTsauWWU1TFbwxe+zclSlHMY8XzorBdkAGsQJGeEHdXuAgUokV0rzMcComvzSfqH4OgVFkNJcfdKlxs5cIylg6Q5UzeCaEqvDAJMPyZoZhvnO5gQ7zsUrTsBlksmLKek78/em1zvbb3d3CCYSPrkXSGMF9iDd8ogEH5W8sutUPzYxWL9un/SSIZpGjqjftmQwZsuXQu5naU2wPT1HZaML6g4WWxuhYD+inCn+xuLPWXB60YDm3M6E8OXM5T6cqve/zWeULnE02+3FJAI8H/FZNlIH8Q8gYuG6arBKV7aCxWq4aA66o2Bcw==',
    'TEST_MSISDN': '254795471321',  # Test phone number
    'ACCOUNT_REFERENCE': 'CloudLink',
    'TRANSACTION_DESC': 'Payment for services',
    'ENVIRONMENT': 'sandbox',
}

# URL Configuration
ROOT_URLCONF = 'cloudlink_devs.urls'

# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# In settings.py
LOGIN_URL = '/client/login/'  # Points to your custom login view

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         #
#         'DIRS': [
#             os.path.join(BASE_DIR, 'templates'),  # Add this line if not already present
#             os.path.join(BASE_DIR, 'client_portal', 'templates'),
#         ],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # Project root templates
            os.path.join(BASE_DIR, 'client_portal', 'templates'),  # App-specific templates
        ],
        'APP_DIRS': True,
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


WSGI_APPLICATION = 'cloudlink_devs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloud',
        'USER': 'root',        # Change this if you have another MySQL user
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}



# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.your-email-provider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'jamhimira@gmail.com'
EMAIL_HOST_PASSWORD = ' xsvy vjls fknj keap'
DEFAULT_FROM_EMAIL = 'CloudLink_Devs <info@cloudlinkdevs.com>'
SITE_URL = 'https://www.cloudlinkdevs.com'  # or http://localhost:8000 for development

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Add to your settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # This points to the project-level templates directory
        'APP_DIRS': True,  # This allows Django to find templates in app-level templates directories
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

PAYPAL_CLIENT_ID = 'your-paypal-client-id'  # For PayPal integration
CRYPTO_ADDRESS = 'your-crypto-wallet-address'  # For crypto payments
ADMIN_EMAIL = 'admin@example.com'  # For email notifications
DEFAULT_FROM_EMAIL = 'jamhimira@gmail.com'  # For sending emails

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#
# # Static files (CSS, JavaScript, Images)
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For production
#
# # Additional locations of static files
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

# Channel layers for WebSocket (for chatbot)
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
        # For production, use Redis instead:
        # 'BACKEND': 'channels_redis.core.RedisChannelLayer',
        # 'CONFIG': {
        #     'hosts': [('127.0.0.1', 6379)],
        # },
    },
}
# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ASGI_APPLICATION = 'cloudlink_devs.asgi.application'
