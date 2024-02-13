from django.contrib import admin
from blok.models import Student

# Register your models here.

# Первый вариант регистрации модели / при её использовании будет только добавление модели
# admin.site.register(Student)


# Второй вариант регистрации модели / Необходима если требуется настройка отображения
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # Как будет выводится
    list_display = ('first_name', 'last_name', 'is_active')

    # Как будет фильтроваться
    list_filter = ('is_active',)

    # Поиск по списку
    search_fields = ('first_name', 'last_name',)


