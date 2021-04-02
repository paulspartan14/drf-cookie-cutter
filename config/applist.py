BEFORE_DJANGO_APPS = (

)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
) 

THIRD_PART_APPS = (
    'drf_yasg',
    'rest_framework',
    'django_filters',
    'corsheaders',  
)

LOCAL_APPS = (
    'titulacion',
)

INSTALLED_APPS = BEFORE_DJANGO_APPS + DJANGO_APPS + THIRD_PART_APPS + LOCAL_APPS  