DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = "Very-Very-Secret"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "university_project",
        'USER': "postgres",
        'PASSWORD': 'nateglass',
        'HOST': "127.0.0.1",
        'PORT': "5432",
    }
}
