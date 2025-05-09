Certainly! Here's the updated project structure with the addition of database migrations:

```
myapp/
├── app/
│   ├── __init__.py
│   ├── main/
│   │   ├── __init__.py
│   │   ├── views.py
│   │   ├── models.py
│   │   └── forms.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── views.py
│   │   ├── models.py
│   │   └── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── main/
│   │   │   ├── index.html
│   │   │   └── ...
│   │   └── auth/
│   │       ├── login.html
│   │       └── ...
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── migrations/
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
│       └── ...
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_auth.py
├── config.py
├── requirements.txt
├── run.py
└── .env
```

The main addition is the `migrations/` directory, which is used for database migrations with Flask-Migrate and Alembic.

- `migrations/`: Contains the database migration files.
  - `alembic.ini`: The configuration file for Alembic.
  - `env.py`: The script that configures the Alembic environment.
  - `README`: A file that provides information about the migrations.
  - `script.py.mako`: A template file used by Alembic to generate migration scripts.
  - `versions/`: Contains the individual migration files generated by Alembic.

To use database migrations in your Flask application, you'll need to install Flask-Migrate and set it up in your application. Here's a general outline of the steps:

1. Install Flask-Migrate:
   ```
   pip install Flask-Migrate
   ```

2. Update `requirements.txt` to include Flask-Migrate.

3. In `app/__init__.py`, initialize Flask-Migrate:
   ```python
   from flask_migrate import Migrate

   migrate = Migrate(app, db)
   ```

4. In `run.py`, add the following imports and commands:
   ```python
   from flask_migrate import MigrateCommand
   from flask_script import Manager

   manager = Manager(app)
   manager.add_command('db', MigrateCommand)

   if __name__ == '__main__':
       manager.run()
   ```

5. Initialize the database migration repository:
   ```
   flask db init
   ```

6. Generate the initial migration:
   ```
   flask db migrate -m "Initial migration"
   ```

7. Apply the migration to the database:
   ```
   flask db upgrade
   ```

Now you have database migrations set up in your Flask application. Whenever you make changes to your models, you can generate a new migration using `flask db migrate` and apply it to the database using `flask db upgrade`.

Remember to update your `requirements.txt` file to include Flask-Migrate, and make sure to follow the Flask-Migrate documentation for more detailed usage instructions.
