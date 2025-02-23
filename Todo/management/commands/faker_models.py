from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.core.management import call_command
from faker import Faker
import random

from django.contrib.auth.models import User
from Todo.models import Category, Author, Task

fake = Faker()

class Command(BaseCommand):
    help = 'Aquest comandament genera dades aleatories'

    # Argument opcional (--flush)
    def add_arguments(self, parser):
        parser.add_argument(
            '--flush',
            help='Eliminar totes les dades base de dades',
            action='store_true'
        )

    # Executa la funció
    def handle(self, *args, **kwargs):
        num_categories = 5
        num_authors = 10
        num_tasks = 20

        self.stdout.write(self.style.SUCCESS(f'Generant {num_categories} categories, {num_authors} users/autors i {num_tasks} tasques utilitzant Faker!'))

        if kwargs['flush']:
            self.stdout.write(self.style.WARNING('I també netejant la base de dades!'))
            call_command('flush', interactive=False)

        categories = []
        for _ in range(num_categories):
            category, _ = Category.objects.get_or_create(name=fake.word(), description=fake.sentence())
            categories.append(category)

        authors = []
        for _ in range(num_authors):
            user, _ = User.objects.get_or_create(username=fake.user_name(), email=fake.email(), password=make_password('1234'))
            author, _ = Author.objects.get_or_create(user=user, dni='12345678X', photo='fallback_avatar.webp')
            authors.append(author)

        for _ in range(num_tasks):
            task, _ = Task.objects.get_or_create(title=fake.sentence(), author=random.choice(authors), completed=random.choice([True, False]))
            task.categories.set(random.sample(categories, random.randint(1, num_categories)))

        self.stdout.write(self.style.SUCCESS('Dades generades correctament!'))
