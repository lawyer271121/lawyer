from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateInput
from .models import News, Answers, Reviews, Gallery
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# При разработке приложения, использующего базу данных, чаще всего необходимо работать с формами, которые аналогичны моделям.
# В этом случае явное определение полей формы будет дублировать код, так как все поля уже описаны в модели.
# По этой причине Django предоставляет вспомогательный класс, который позволит вам создать класс Form по имеющейся модели
# атрибут fields - указание списка используемых полей, при fields = '__all__' - все поля
# атрибут widgets для указания собственный виджет для поля. Его значением должен быть словарь, ключами которого являются имена полей, а значениями — классы или экземпляры виджетов.
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('daten', 'title', 'details', 'photo')
        widgets = {
            'daten': DateInput(attrs={"type":"date"}),
            'title': TextInput(attrs={"size":"100"}),
            'details': Textarea(attrs={'cols': 80, 'rows': 10}),            
        }

class AnswersFormCreate(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ({'question',})
        widgets = {
            'question': Textarea(attrs={'cols': 80, 'rows': 10}),
        }
    
class AnswersFormEdit(forms.ModelForm):
    class Meta:
        model = Answers
        fields = ('datea', 'question', 'answer', 'user', 'specialist')
        widgets = {
            'datea': TextInput(attrs={"type":"date", "readonly": "readonly"}),
            'question': Textarea(attrs={'cols': 80, 'rows': 10, "readonly": "readonly"}),
            'answer': Textarea(attrs={'cols': 80, 'rows': 10}),
            'user': TextInput(attrs={"readonly": "readonly"}),
            'specialist': TextInput(attrs={"readonly": "readonly"}),
        }

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ({'details',})
        widgets = {
            'details': Textarea(attrs={'cols': 80, 'rows': 10}),            
        }

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('dateg', 'title', 'details', 'photo')
        widgets = {
            'dateg': DateInput(attrs={"type":"date"}),
            'title': TextInput(attrs={"size":"100"}),
            'details': Textarea(attrs={'cols': 80, 'rows': 10}),            
        }
        
# Форма регистрации
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
