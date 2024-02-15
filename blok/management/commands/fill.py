from django.core.management import BaseCommand
from blok.models import Student

# Команда для запуска заполнения - python manage.py fill
class Command(BaseCommand):
    def handle(self, *args, **options):
        students_list = [
            {'last_name': 'Ivanov', 'first_name': 'Ivan'},
            {'last_name': 'Petrov', 'first_name': 'Petr'},
            {'last_name': 'Sıdorov', 'first_name': 'Mıhaıl'},
            {'last_name': 'Aleksandrov', 'first_name': 'Dmıtrıy'}

        ]

# Первый вариант добавления в таблицу, при нем команда craete срабатывает при каждом добавлении.
        # for student_item in students_list:
        #     Student.objects.create(**student_item)

#  Второй вариант - через первоначальное создание листа:
        students_for_create = []
        for student_item in students_list:
            students_for_create.append(Student(**student_item))

        Student.objects.bulk_create(students_for_create)
