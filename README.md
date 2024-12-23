# postsDjango
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django)


## Установка
### Перейдите в репозиторию где будет развернут проект и инициализируйте новый репозиторий GIT и клонируйте проект с git: 
```commandline
git init
git clone 'https://github.com/репозиторий.git'
```
### Создание виртуального окружения:
```commandline
python3 -m venv venv
```
### Активируйте виртуальное окружение:
```commandline
source venv/bin/activate
```
### Устанавливаем библиотеки из файла [requirements.txt]
```commandline
pip install -r requirements.txt
```

## Запускаем проект
Запускаем приложение с директории проекта
```commandline
python manage.py runserver  
```
## Запускаем команду загрузки [Данных](https://jsonplaceholder.typicode.com/posts)
```commandline
python manage.py parse_data
```

