DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'afpa_car3',
        'USER': 'pc_Boris',
        'PASSWORD': '',
        'HOST': '10.111.62.2',
        'PORT': '',
        'OPTIONS': {
        "init_command": "SET foreign_key_checks = 0;",
        },
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'afpa_car_maison',
#     }
# }