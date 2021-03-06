# Todo App

A simple todo app built with django

demo - http://ll220l0-todo-demo.herokuapp.com/login/?next=/

## Setup

```bash
git clone https://github.com/ll220l0/todo_app.git
cd todo_app
```

Create file **.env** :
```
SECRET_KEY=your_django_secret_key
DEBUG=debug
ALLOWED_HOSTS=allowed_hosts
DB_USER=your_postgres_user
DB_PASS=your_postgres_user_password
DB_NAME=your_postgres_database_name
DB_HOST=db_host
DB_PORT=db_port
```

You will need django to be installed in you computer to run this app. 

```bash
python3 -m venv env
source env/bin/activate

pip3 install -r requirements.txt
```

Once you have downloaded django, go to the cloned repo directory and run the following command

```bash
python3 manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```
python3 manage.py migrate
```

One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user

```
python3 manage.py createsuperuser
```

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our simple todo App. Start the server by following command

```
python manage.py runserver
```

Once the server is hosted, head over to http://127.0.0.1:8000  for the App.

Cheers and Happy Coding :)
