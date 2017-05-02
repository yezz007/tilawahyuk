SECRET_KEY = 't8=f%7nrkhiyere4h_z!@24a5(8^e&)*nq67c8o0ku+zn3(vr!' #of course, different key is used on production
LINE_CHANNEL_ACCESS_TOKEN = 'this_is_useless_in_local_development'
LINE_CHANNEL_SECRET = 'this_is_useless_in_local_development'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tilawah',
        'USER': 'django',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}