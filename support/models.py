from django.db import models
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _

from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from django.core.files.storage import default_storage as storage

from django.contrib.auth.models import User

# Модели отображают информацию о данных, с которыми вы работаете.
# Они содержат поля и поведение ваших данных.
# Обычно одна модель представляет одну таблицу в базе данных.
# Каждая модель это класс унаследованный от django.db.models.Model.
# Атрибут модели представляет поле в базе данных.
# Django предоставляет автоматически созданное API для доступа к данным

# choices (список выбора). Итератор (например, список или кортеж) 2-х элементных кортежей,
# определяющих варианты значений для поля.
# При определении, виджет формы использует select вместо стандартного текстового поля
# и ограничит значение поля указанными значениями.

# Новости 
class News(models.Model):
    # Читабельное имя поля (метка, label). Каждое поле, кроме ForeignKey, ManyToManyField и OneToOneField,
    # первым аргументом принимает необязательное читабельное название.
    # Если оно не указано, Django самостоятельно создаст его, используя название поля, заменяя подчеркивание на пробел.
    # null - Если True, Django сохранит пустое значение как NULL в базе данных. По умолчанию - False.
    # blank - Если True, поле не обязательно и может быть пустым. По умолчанию - False.
    # Это не то же что и null. null относится к базе данных, blank - к проверке данных.
    # Если поле содержит blank=True, форма позволит передать пустое значение.
    # При blank=False - поле обязательно.
    daten = models.DateTimeField(_('daten'))
    title = models.CharField(_('title_news'), max_length=256)
    details = models.TextField(_('details_news'))
    photo = models.ImageField(_('photo_news'), upload_to='images/', blank=True, null=True)    
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'news'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['daten']),
        ]
        # Сортировка по умолчанию
        ordering = ['daten']
    #def save(self):
    #    super().save()
    #    img = Image.open(self.photo.path) # Open image
    #    # resize image
    #    if img.width > 512 or img.height > 700:
    #        proportion_w_h = img.width/img.height  # Отношение ширины к высоте 
    #        output_size = (512, int(512/proportion_w_h))
    #        img.thumbnail(output_size) # Изменение размера
    #        img.save(self.photo.path) # Сохранение

# Ответы на вопросы 
class Answers(models.Model):
    datea = models.DateTimeField(_('datea'))
    question = models.TextField(_('question'))
    answer = models.TextField(_('answer'), blank=True, null=True)
    user = models.ForeignKey(User, related_name='user_answers', on_delete=models.CASCADE)
    specialist = models.ForeignKey(User, blank=True, null=True, related_name='specialist_answers', on_delete=models.CASCADE)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'answers'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['datea']),
        ]
        # Сортировка по умолчанию
        ordering = ['datea']

# Отзывы 
class Reviews(models.Model):
    dater = models.DateTimeField(_('dater'))
    details = models.TextField(_('details_reviews'))
    user = models.ForeignKey(User, related_name='user_reviews', on_delete=models.CASCADE)
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'reviews'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['dater']),
        ]
        # Сортировка по умолчанию
        ordering = ['dater']
    
# Галерея 
class Gallery(models.Model):
    dateg = models.DateTimeField(_('dateg'))
    title = models.CharField(_('title_gallery'), max_length=256)
    details = models.TextField(_('details_gallery'))
    photo = models.ImageField(_('photo_gallery'), upload_to='images/', blank=True, null=True)    
    class Meta:
        # Параметры модели
        # Переопределение имени таблицы
        db_table = 'gallery'
        # indexes - список индексов, которые необходимо определить в модели
        indexes = [
            models.Index(fields=['dateg']),
        ]
        # Сортировка по умолчанию
        ordering = ['dateg']
    #def save(self):
    #    super().save()
    #    img = Image.open(self.photo.path) # Open image
    #    # resize image
    #    if img.width > 512 or img.height > 700:
    #        proportion_w_h = img.width/img.height  # Отношение ширины к высоте 
    #        output_size = (512, int(512/proportion_w_h))
    #        img.thumbnail(output_size) # Изменение размера
    #        img.save(self.photo.path) # Сохранение
