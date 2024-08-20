# Django DB Optimization test setup

## Dev setup

1. Clone repo
2. Create python venv `python3 -m venv venv`
3. Install all pip dependencies `pip install -r requirements.txt`
4. Setup django db

```bash
# Migrate
python manage.py migrate

# Create super user
python manage.py createsuperuser

# Add sample data to seed DB for test queries
python manage.py setup_sample_data

# Run server in dev mode
python manage.py runserver 8001
```

6. The server should now be up, and admin portal should be available at [http://localhost:8001/admin]()

# Minhas anotações
Admin
username: catalunha
senha: drf@1234

Artigo deste repo
https://python.plainenglish.io/django-orm-mastering-performance-with-select-related-and-prefetch-related-48c0958fe8be