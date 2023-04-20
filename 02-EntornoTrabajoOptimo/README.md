## Steps for create project django

- 1 Create entorno virtual
- 2 Instalar Django
  - dentro de la carpteta de **Scripts** del entorno
  - ```` pip install django````
- 3 Crear el proyecto
  - al nivel de la carpeta del entorno virtual
  - ````django-admin startproject nombre_proyecto````
- 4 Correr el proyecto
  - ````python manage.py runserver````
  - Asignando el puerto
  - ````python manage.py runserver 8080```` 
-5 Crear una app
  - ```python manage.py startapp nombre_app```
  - ```django-admin startapp nombre_app```