# MARIADB
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'afpa_car2',
#         'USER': 'pc_Boris',
#         'PASSWORD': '',
#         'HOST': '10.111.62.2',
#         'PORT': '',
#         'OPTIONS': {
#         "init_command": "SET foreign_key_checks = 0;",
#         },
#     }
# }


#SQLITE3
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}
