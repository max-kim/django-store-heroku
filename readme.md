# Django маркет (demo)

Демонстрационная версия Django маркета.

## Требования

- Python 3.6 (or over)
- SQLite 3
- Django 2.1.1
- whitenoise 3.3.1

## Установка

Для устаовки Django маркета выполните в терминале следующие команды:
```bash
    $ mkdir <installation dir>
    $ cd <installation dir>
    $ git clone git://github.com/max-kim/django-store.git
    $ cd django-store
    $ ./manage.py migrate
    $ ./manage.py collectstatic
    $ ./manage.py init_demo

```

По команде "init_demo" будет произведено заполнение базы Django маркета
демонстрационными данными.

Также демо-версия Django маркета доступна на платформе [Heroku](https://django-store-demo.herokuapp.com/).

## Запуск сервера

Для запуска web-сервера выполните в терминале следующую команду:
```bash
    $ ./manage.py runserver
```

Затем в браузере перейдите по адресу: ['localhost:8000'](http://localhost:8000)

## Прочее
Данная демонстационная версия Django маркета является домашней работой на курсе OTUS Python web-dev.
