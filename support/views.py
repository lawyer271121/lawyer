from django.shortcuts import render, redirect

# Класс HttpResponse из пакета django.http, который позволяет отправить текстовое содержимое.
from django.http import HttpResponse
# Конструктор принимает один обязательный аргумент – путь для перенаправления. Это может быть полный URL (например, 'https://www.yahoo.com/search/') или абсолютный путь без домена (например, '/search/').
from django.http import HttpResponseRedirect

from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Подключение моделей
from .models import News, Answers, Reviews, Gallery
# Подключение форм
from .forms import NewsForm, AnswersFormCreate, AnswersFormEdit, ReviewsForm, GalleryForm
from .forms import SignUpForm

import datetime

import xlwt
from io import BytesIO

from django.db import models

import sys

#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _

from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy

from django.contrib.auth import login as auth_login

 
def index(request):
    reviews = Reviews.objects.all().order_by('?')[:3]
    return render(request, "index.html", {"reviews": reviews})

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

def sample(request):
    return render(request, "sample.html")

def link(request):
    return render(request, "link.html")

# Групповые ограничения
def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, login_url='403')

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def news_index(request):
    #news = News.objects.all().order_by('surname', 'name', 'patronymic')
    #return render(request, "news/index.html", {"news": news})
    news = News.objects.all().order_by('-daten')
    return render(request, "news/index.html", {"news": news})

# Список для просмотра
def news_list(request):
    news = News.objects.all().order_by('-daten')
    return render(request, "news/list.html", {"news": news})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def news_create(request):
    if request.method == "POST":
        news = News()        
        news.daten = request.POST.get("daten")
        news.title = request.POST.get("title")
        news.details = request.POST.get("details")
        if 'photo' in request.FILES:                
            news.photo = request.FILES['photo']        
        news.save()
        return HttpResponseRedirect(reverse('news_index'))
    else:        
        newsform = NewsForm(request.FILES)
        return render(request, "news/create.html", {"form": newsform})

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
# И вначале по этому идентификатору мы пытаемся найти объект с помощью метода News.objects.get(id=id).
# Поскольку в случае отсутствия объекта мы можем столкнуться с исключением News.DoesNotExist,
# то соответственно нам надо обработать подобное исключение, если вдруг будет передан несуществующий идентификатор.
# И если объект не будет найден, то пользователю возващается ошибка 404 через вызов return HttpResponseNotFound().
# Если объект найден, то обработка делится на две ветви.
# Если запрос POST, то есть если пользователь отправил новые изменненые данные для объекта, то сохраняем эти данные в бд и выполняем переадресацию на корень веб-сайта.
# Если запрос GET, то отображаем пользователю страницу edit.html с формой для редактирования объекта.
@login_required
@group_required("Managers")
def news_edit(request, id):
    try:
        news = News.objects.get(id=id) 
        if request.method == "POST":
            news.daten = request.POST.get("daten")
            news.title = request.POST.get("title")
            news.details = request.POST.get("details")
            if "photo" in request.FILES:                
                news.photo = request.FILES["photo"]
            news.save()
            return HttpResponseRedirect(reverse('news_index'))
        else:
            # Загрузка начальных данных
            newsform = NewsForm(initial={'daten': news.daten.strftime('%Y-%m-%d'), 'title': news.title, 'details': news.details, 'photo': news.photo })
            return render(request, "news/edit.html", {"form": newsform})
    except News.DoesNotExist:
        return HttpResponseNotFound("<h2>News not found</h2>")

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def news_delete(request, id):
    try:
        news = News.objects.get(id=id)
        news.delete()
        return HttpResponseRedirect(reverse('news_index'))
    except News.DoesNotExist:
        return HttpResponseNotFound("<h2>News not found</h2>")

# Просмотр страницы read.html для просмотра объекта.
@login_required
def news_read(request, id):
    try:
        news = News.objects.get(id=id) 
        return render(request, "news/read.html", {"news": news})
    except News.DoesNotExist:
        return HttpResponseNotFound("<h2>News not found</h2>")

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def answers_index(request):
    answers = Answers.objects.all().order_by('-datea')
    return render(request, "answers/index.html", {"answers": answers})

# Список для просмотра
def answers_list(request):
    answers = Answers.objects.all().order_by('-datea')
    return render(request, "answers/list.html", {"answers": answers})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
def answers_create(request):
    if request.method == "POST":
        # Текущий пользователь
        _user_id = request.user.id
        answers = Answers()        
        answers.datea = datetime.datetime.now()
        answers.question = request.POST.get("question")
        answers.user_id = _user_id
        answers.save()
        return HttpResponseRedirect(reverse('answers_list'))
    else:        
        answersform = AnswersFormCreate(request.FILES)
        return render(request, "answers/create.html", {"form": answersform})

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
# И вначале по этому идентификатору мы пытаемся найти объект с помощью метода Answers.objects.get(id=id).
# Поскольку в случае отсутствия объекта мы можем столкнуться с исключением Answers.DoesNotExist,
# то соответственно нам надо обработать подобное исключение, если вдруг будет передан несуществующий идентификатор.
# И если объект не будет найден, то пользователю возващается ошибка 404 через вызов return HttpResponseNotFound().
# Если объект найден, то обработка делится на две ветви.
# Если запрос POST, то есть если пользователь отправил новые изменненые данные для объекта, то сохраняем эти данные в бд и выполняем переадресацию на корень веб-сайта.
# Если запрос GET, то отображаем пользователю страницу edit.html с формой для редактирования объекта.
@login_required
@group_required("Managers")
def answers_edit(request, id):
    try:
        # Текущий пользователь
        _user_id = request.user.id
        
        answers = Answers.objects.get(id=id) 
        if request.method == "POST":
            answers.datea = request.POST.get("datea")
            answers.answer = request.POST.get("answer")
            answers.specialist_id = _user_id
            answers.save()
            return HttpResponseRedirect(reverse('answers_index'))
        else:
            # Загрузка начальных данных
            print(answers.specialist)
            if answers.specialist is None:                
                answersform = AnswersFormEdit(initial={'datea': answers.datea.strftime('%Y-%m-%d'), 'question': answers.question, 'answer': answers.answer, 'user': answers.user.username, 'specialist': answers.specialist })
            else:
                answersform = AnswersFormEdit(initial={'datea': answers.datea.strftime('%Y-%m-%d'), 'question': answers.question, 'answer': answers.answer, 'user': answers.user.username, 'specialist': answers.specialist.username  })
            return render(request, "answers/edit.html", {"form": answersform})
    except Answers.DoesNotExist:
        return HttpResponseNotFound("<h2>Answers not found</h2>")

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def answers_delete(request, id):
    try:
        answers = Answers.objects.get(id=id)
        answers.delete()
        return HttpResponseRedirect(reverse('answers_index'))
    except Answers.DoesNotExist:
        return HttpResponseNotFound("<h2>Answers not found</h2>")

# Просмотр страницы read.html для просмотра объекта.
@login_required
def answers_read(request, id):
    try:
        answers = Answers.objects.get(id=id) 
        return render(request, "answers/read.html", {"answers": answers})
    except Answers.DoesNotExist:
        return HttpResponseNotFound("<h2>Answers not found</h2>")

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def reviews_index(request):
    reviews = Reviews.objects.all().order_by('dater')
    return render(request, "reviews/index.html", {"reviews": reviews})

# Список для просмотра
def reviews_list(request):
    reviews = Reviews.objects.all().order_by('dater')
    return render(request, "reviews/list.html", {"reviews": reviews})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
def reviews_create(request):
    if request.method == "POST":
        # Текущий пользователь
        _user_id = request.user.id
        reviews = Reviews()        
        reviews.dater =  datetime.datetime.now()
        reviews.details = request.POST.get("details")
        reviews.user_id = _user_id
        reviews.save()
        return HttpResponseRedirect(reverse('reviews_list'))
    else:        
        reviewsform = ReviewsForm(request.FILES)
        return render(request, "reviews/create.html", {"form": reviewsform})

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
# И вначале по этому идентификатору мы пытаемся найти объект с помощью метода Reviews.objects.get(id=id).
# Поскольку в случае отсутствия объекта мы можем столкнуться с исключением Reviews.DoesNotExist,
# то соответственно нам надо обработать подобное исключение, если вдруг будет передан несуществующий идентификатор.
# И если объект не будет найден, то пользователю возващается ошибка 404 через вызов return HttpResponseNotFound().
# Если объект найден, то обработка делится на две ветви.
# Если запрос POST, то есть если пользователь отправил новые изменненые данные для объекта, то сохраняем эти данные в бд и выполняем переадресацию на корень веб-сайта.
# Если запрос GET, то отображаем пользователю страницу edit.html с формой для редактирования объекта.
@login_required
@group_required("Managers")
def reviews_edit(request, id):
    try:
        # Текущий пользователь
        _user_id = request.user.id
        
        reviews = Reviews.objects.get(id=id) 
        if request.method == "POST":
            reviews.dater = request.POST.get("dater")
            reviews.details = request.POST.get("details")
            reviews.user_id = _user_id
            reviews.save()
            return HttpResponseRedirect(reverse('reviews_index'))
        else:
            # Загрузка начальных данных
            reviewsform = ReviewsForm(initial={'dater': reviews.dater.strftime('%Y-%m-%d'), 'details': reviews.details, 'user': reviews.user  })
            return render(request, "reviews/edit.html", {"form": reviewsform})
    except Reviews.DoesNotExist:
        return HttpResponseNotFound("<h2>Reviews not found</h2>")

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def reviews_delete(request, id):
    try:
        reviews = Reviews.objects.get(id=id)
        reviews.delete()
        return HttpResponseRedirect(reverse('reviews_index'))
    except Reviews.DoesNotExist:
        return HttpResponseNotFound("<h2>Reviews not found</h2>")

# Просмотр страницы read.html для просмотра объекта.
@login_required
def reviews_read(request, id):
    try:
        reviews = Reviews.objects.get(id=id) 
        return render(request, "reviews/read.html", {"reviews": reviews})
    except Reviews.DoesNotExist:
        return HttpResponseNotFound("<h2>Reviews not found</h2>")

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def gallery_index(request):
    #gallery = Gallery.objects.all().order_by('surname', 'name', 'patronymic')
    #return render(request, "gallery/index.html", {"gallery": gallery})
    gallery = Gallery.objects.all().order_by('dateg')
    return render(request, "gallery/index.html", {"gallery": gallery})

# Список для просмотра
def gallery_list(request):
    gallery = Gallery.objects.all().order_by('dateg')
    return render(request, "gallery/list.html", {"gallery": gallery})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def gallery_create(request):
    if request.method == "POST":
        gallery = Gallery()        
        gallery.dateg = request.POST.get("dateg")
        gallery.title = request.POST.get("title")
        gallery.details = request.POST.get("details")
        if 'photo' in request.FILES:                
            gallery.photo = request.FILES['photo']        
        gallery.save()
        return HttpResponseRedirect(reverse('gallery_index'))
    else:        
        galleryform = GalleryForm(request.FILES)
        return render(request, "gallery/create.html", {"form": galleryform})

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
# И вначале по этому идентификатору мы пытаемся найти объект с помощью метода Gallery.objects.get(id=id).
# Поскольку в случае отсутствия объекта мы можем столкнуться с исключением Gallery.DoesNotExist,
# то соответственно нам надо обработать подобное исключение, если вдруг будет передан несуществующий идентификатор.
# И если объект не будет найден, то пользователю возващается ошибка 404 через вызов return HttpResponseNotFound().
# Если объект найден, то обработка делится на две ветви.
# Если запрос POST, то есть если пользователь отправил новые изменненые данные для объекта, то сохраняем эти данные в бд и выполняем переадресацию на корень веб-сайта.
# Если запрос GET, то отображаем пользователю страницу edit.html с формой для редактирования объекта.
@login_required
@group_required("Managers")
def gallery_edit(request, id):
    try:
        gallery = Gallery.objects.get(id=id) 
        if request.method == "POST":
            gallery.dateg = request.POST.get("dateg")
            gallery.title = request.POST.get("title")
            gallery.details = request.POST.get("details")
            if "photo" in request.FILES:                
                gallery.photo = request.FILES["photo"]
            gallery.save()
            return HttpResponseRedirect(reverse('gallery_index'))
        else:
            # Загрузка начальных данных
            galleryform = GalleryForm(initial={'dateg': gallery.dateg.strftime('%Y-%m-%d'), 'title': gallery.title, 'details': gallery.details, 'photo': gallery.photo })
            return render(request, "gallery/edit.html", {"form": galleryform})
    except Gallery.DoesNotExist:
        return HttpResponseNotFound("<h2>Gallery not found</h2>")

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def gallery_delete(request, id):
    try:
        gallery = Gallery.objects.get(id=id)
        gallery.delete()
        return HttpResponseRedirect(reverse('gallery_index'))
    except Gallery.DoesNotExist:
        return HttpResponseNotFound("<h2>Gallery not found</h2>")

# Просмотр страницы read.html для просмотра объекта.
@login_required
def gallery_read(request, id):
    try:
        gallery = Gallery.objects.get(id=id) 
        return render(request, "gallery/read.html", {"gallery": gallery})
    except Gallery.DoesNotExist:
        return HttpResponseNotFound("<h2>Gallery not found</h2>")

# Регистрационная форма 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
            #return render(request, 'registration/register_done.html', {'new_user': user})
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email',)
    template_name = 'registration/my_account.html'
    success_url = reverse_lazy('index')
    #success_url = reverse_lazy('my_account')
    def get_object(self):
        return self.request.user

