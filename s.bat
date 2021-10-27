pip3 freeze > requirements.txt
python manage.py migrate     					
python manage.py makemigrations users
python manage.py makemigrations support
python manage.py makemigrations
python manage.py migrate
python manage.py check
python manage.py runserver 