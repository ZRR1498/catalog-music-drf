# Music catalog
This API is a music catalog that includes artists, artists' albums, and their songs.

### Main functionality:
* **Creating, editing and deleting performers**
* **Creating, editing and deleting albums linked to artists**
* **Creating, editing and deleting songs linked to albums**

### Requirements
* Language: **Python 3.11**
* Framework: **Django 4.1.17** and **Django Rest Framework 3.14.0**
* Database: **PostgreSQL 15**

## Preparing
Create **.env** file in the main music_catalog directory and fill it in as in the example .env.example:

        SECRET_KEY='secret_key'
        DB_USERNAME=postgres
        DB_PASSWORD=postgres
        DB_NAME=postgres
        DB_HOST=db
        DB_PORT=5432

## Application launch
Run the following command in a terminal:

    docker-compose up

Then go into the application container by running the following command:
    
    docker exec -it backend_api sh

Run the migrations:

    python manage.py migrate

Create a superuser:
    
    python manage.py createsuperuser

### All done!