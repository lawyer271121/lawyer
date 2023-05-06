from django.contrib import admin
# Импорт модели
from .models import News
from .models import Answers
from .models import Reviews
from .models import Gallery
# Добавление модели на главную страницу интерфейса администратора
admin.site.register(News)
admin.site.register(Answers)
admin.site.register(Reviews)
admin.site.register(Gallery)


