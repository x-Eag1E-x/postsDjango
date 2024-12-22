import requests
from django.core.management.base import BaseCommand
from posts.models import Post

class Command(BaseCommand):
    help = 'Загружает данные из API в базу данных'
    def handle(self, *args, **kwargs):
        url = 'https://jsonplaceholder.typicode.com/posts'

        try:
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            for item in data:
                Post.objects.create(
                    id=item['id'],
                    title=item['title'],
                    userId=item['userId'],
                    body=item['body']
                )

            self.stdout.write(self.style.SUCCESS('Данные успешно загружены!'))
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при запросе к API: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при обработке данных: {e}'))
