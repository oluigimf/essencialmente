PC da Escola:
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'essencialmente',
'USER': 'root',
'PASSWORD': '1234',
'HOST': 'localhost',
'PORT': '3306'
}
}

PC do Luigi:
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'essencialmente',
'USER': 'postgres',
'PASSWORD': 'postgres',
'HOST': 'localhost',
'PORT': '5432'
}
}

PC do Piccoli:
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'essencialmente',
'USER': 'postgres',
'PASSWORD': 'metzdorf',
'HOST': 'localhost',
'PORT': '5432'
}
}
