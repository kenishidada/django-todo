# todolist api

## start command

```
git clone https://github.com/kenishidada/django-todo.git
cd django-todo
// 仮想環境作成
python3 -m venv
source venv/bin/activate
// DB初期設定
python manage.py makemigrations
python manage.py migrate
// superuser作成
python manage.py createsuperuser
// runserver
python manage.py runserver


localhost:8000/admin
              /list
              /detail/<id>
              /create
              /update
              /delete

```
