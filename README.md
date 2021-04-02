
#### Asegurarse tener entorno virtual instalado con python 3.7

`virtualenv env`

Instalar requirements

`pip install -r requirements.txt`

Crear nuevo proyecto django

`django-admin startproject config .`

crear application (modules)

`django-admin startapp blog`

--- correr server ---

`python manage.py runserver`

creando super-usuario

`python manage.py createsuperuser`

--- crear migraciones ---

`python manage.py makemigrations`

--- correr migraciones ---

`python manage.py migrate` 

--- correr tests ---

`python manage.py test`


-- importar variables virtuales al so develop --

`source .env.local`