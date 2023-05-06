from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import migrations

from datetime import datetime, timedelta
import time

def beginning(apps, schema_editor):

    user = User.objects.create_superuser(username='root',
    email='lawyer271121@mail.ru',
    password='SsNn5678+-@', 
    last_login=datetime.now())
    print("Суперпользователь создан")
    
    # Группа менеджеров
    managers = Group.objects.get_or_create(name = 'Managers')
    managers = Group.objects.get(name='Managers')
    print("Группа менеджеров создана")
    
    # Пользователь с ролью менеджера id2
    user = User.objects.create_user(username='manager', password='Ss0066+-', email='manager@mail.ru', first_name='Менеджер', last_name='', last_login=datetime.now())
    managers.user_set.add(user)
    print("Менеджер добавлен в группу менеджеров")

    user = User.objects.create_user(username='user1', password='Uu0066+-', email='user1@mail.ru', first_name='Дина', last_name='Мусина', last_login=datetime.now())
    user = User.objects.create_user(username='user2', password='Uu0066+-', email='user2@mail.ru', first_name='Адия', last_name='Жунусова', last_login=datetime.now())
    user = User.objects.create_user(username='user3', password='Uu0066+-', email='user3@mail.ru', first_name='Айнура', last_name='Кенина', last_login=datetime.now())
    user = User.objects.create_user(username='user4', password='Uu0066+-', email='user4@mail.ru', first_name='Рустем', last_name='Какимов', last_login=datetime.now())
    user = User.objects.create_user(username='user5', password='Uu0066+-', email='user5@mail.ru', first_name='Алишер', last_name='Кабдуалиев', last_login=datetime.now())

    ##### Новости #####
    
    News = apps.get_model("support", "News")
   
    news = News()
    news.id = 1
    news.daten = datetime.now() - timedelta(days=60)
    news.title = 'Президент Токаев подписал два закона по вопросам безопасности в СНГ'
    news.details = 'Президент Касым-Жомарт Токаев подписал два закона, направленных на обеспечение безопасности на пространстве стран СНГ, передает Tengrinews.kz со ссылкой на сайт Акорды. Главой государства подписан закон "О ратификации Соглашения о Совместной (объединенной) системе связи вооруженных сил государств - участников Содружества Независимых Государств" и закон "О ратификации Соглашения о Совместном инженерном подразделении гуманитарного разминирования вооруженных сил государств - участников СНГ". Ранее заместитель министра обороны Тимур Дандыбаев объяснял, что первое соглашение предусматривает создание совместной объединенной системы связи вооруженных сил, основными задачами которой являются предоставление услуг связи и обеспечение обмена всеми видами информации в системе управления вооруженных сил и между вооруженными силами стран. По его словам, в целях обеспечения функционирования совместной объединенной системы связи могут использоваться ресурсы сетей связи вооруженных сил государств-участников.'
    news.photo = 'images/news1.jpeg'
    news.save()

    news = News()
    news.id = 2
    news.daten = datetime.now() - timedelta(days=50)
    news.title = 'Сенаторы попросили усилить меры безопасности при хранении боеприпасов'
    news.details = 'Законопроект о госзакупках вернули на доработку в Мажилис. Сенаторы предложили внести в действующее законодательство новую норму по обеспечению безопасности людей и предотвращению взрывов на оружейных складах, передает корреспондент Tengrinews.kz. Депутаты Сената вернули проект Закона "О внесении изменений и дополнений в некоторые законодательные акты Республики Казахстан по вопросам государственных закупок, закупок недропользователей и субъектов естественных монополий, связи, автомобильного транспорта и обороны" в Мажилис с поправками. На заседании Сената депутаты озвучили необходимость усиления мер безопасности при хранении боеприпасов.'
    news.photo = 'images/news2.jpeg'
    news.save()

    news = News()
    news.id = 3
    news.daten = datetime.now() - timedelta(days=45)
    news.title = 'Казахстан ратифицировал протокол о защите Каспия от загрязнения'
    news.details = 'Президент Касым-Жомарт Токаев подписал закон о ратификации протокола по защите Каспия от загрязнения из наземных источников и в результате осуществляемой на суше деятельности к Рамочной конвенции по защите морской среды Каспийского моря, передает Tengrinews.kz со ссылкой на сайт Акорды. "Главой государства подписан закон Республики Казахстан "О ратификации протокола по защите Каспийского моря от загрязнения из наземных источников и в результате осуществляемой на суше деятельности к Рамочной конвенции по защите морской среды Каспийского моря", - говорится в сообщении.'
    news.photo = 'images/news3.jpeg'
    news.save()

    news = News()
    news.id = 4
    news.daten = datetime.now() - timedelta(days=40)
    news.title = 'Регулирование мобильных переводов: что изменится в Налоговом кодексе'
    news.details = 'Норма о регулировании мобильных переводов вошла в законопроект "О внесении изменений и дополнений в Кодекс Республики Казахстан "О налогах и других обязательных платежах в бюджет" (Налоговый кодекс) и Закон Республики Казахстан "О введении в действие Кодекса Республики Казахстан "О налогах и других обязательных платежах в бюджет". В рамках обсуждения депутат Аманжан Жамалов спросил, что ждать потребителям и предпринимателям от новой нормы, не усилится ли налоговая нагрузка на бизнесменов. "Некоторые из субъектов предпринимательства не исполняют свои налоговые обязательства, не проводят фискализацию чеков, соответственно, не показывают обороты и уходят, скрывают доходы, уклоняются от уплаты налогов. В данном законопроекте мы сейчас конкретизируем понятие, что такое мобильные платежи. Это одна из форм платежей, которая сейчас вводится в Налоговый кодекс. Сейчас у нас в Налоговом кодексе предусмотрены только две формы оплаты - наличными средствами и путем карточного перевода через POS-терминалы с обязательным выбиванием фискального чека при предоставлении товаров и оказания работ, услуг", - ответил депутат Сергей Симонов. '
    news.photo = 'images/news4.jpeg'
    news.save()

    news = News()
    news.id = 5
    news.daten = datetime.now() - timedelta(days=35)
    news.title = 'Закон по содержанию кладбищ предложили разработать в Казахстане'
    news.details = 'Разработать законопроект для регулирования вопросов погребения, размещения и содержания кладбищ предложил депутат Сената, передает корреспондент Tengrinews.kz. Сенатор Едил Мамытбеков в своем депутатском запросе премьер-министру Аскару Мамину озвучил проблемы, касающиеся захоронений и содержания кладбищ. Он напомнил, что еще в 2017 году сенатор Ольга Перепечина озвучивала запрос о необходимости разработки законопроекта "О погребении и похоронном деле". Однако, как подчеркнул сенатор, профильные госорганы этот вопрос проигнорировали и заволокитили. Между тем, по словам Мамытбекова, отсутствие законодательного акта сейчас "может привести к проблемам в будущем". "В Казахстане стали появляться частные фирмы, оказывающие ритуальные услуги. Их количество растет как на дрожжах. Принятие закона позволит не только контролировать такую важную отрасль, но и сделать ее доступной. По мнению экспертов, отсутствие законодательного акта, регулирующего вопросы погребения, приводит к различным правонарушениям. Не исключены факты криминального захоронения, ведение незаконного бизнеса, отсутствует четкий регламент эксгумации и захоронения", - подчеркнул сенатор.'
    news.photo = 'images/news5.jpeg'
    news.save()

    ##### Вопрос-ответ #####
    Answers = apps.get_model("support", "answers")
    
    answers = Answers()
    answers.id = 1
    answers.datea = datetime.now() - timedelta(days=30)
    answers.question = 'Обязательно ли заключение трудового договора с работником?'
    answers.answer = 'В соответствии с пунктом 1 статьи 10 Трудового Кодекса РК Трудовые отношения, а также иные отношения, непосредственно связанные с трудовыми, регулируются трудовым договором, актом работодателя, соглашением и коллективным договором. Допуск работодателем к работе лица без заключения трудового договора является административным правонарушением и влечет административную ответственность в виде штрафа по статье 86 Кодекса РК об административных правонарушениях в размере от двадцати до двухсот месячных расчетных показателей в зависимости от тяжести правонарушения. Таким образом, заключение трудового договора с работником является обязательным.'
    answers.user_id = 3
    answers.specialist_id = 1
    answers.save()

    answers = Answers()
    answers.id = 2
    answers.datea = datetime.now() - timedelta(days=25)
    answers.question = 'Как заключать трудовой договор с несовершеннолетним?'
    answers.answer = 'Согласно статьи 30 Трудового Кодекса РК заключение трудового договора допускается с гражданами, достигшими шестнадцатилетнего возраста. С гражданами, достигшими пятнадцати лет, в случаях получения ими основного среднего, общего среднего образования в организации среднего образования; учащимися, достигшими четырнадцатилетнего возраста, для выполнения в свободное от учебы время работы, не причиняющей вреда здоровью и не нарушающей процесса обучения; с лицами, не достигшими четырнадцатилетнего возраста, в организациях кинематографии, театрах, театральных и концертных организациях, цирках для участия в создании и (или) исполнении произведений без ущерба здоровью и нравственному развитию, допускается заключение трудового договора только с письменного согласия одного из родителей, опекуна, попечителя или усыновителя.'
    answers.user_id = 4
    answers.specialist_id = 2
    answers.save()

    answers = Answers()
    answers.id = 3
    answers.datea = datetime.now() - timedelta(days=20)
    answers.question = 'Имеет ли право работодатель требовать выполнения дополнительной работы?'
    answers.answer = 'В силу статьи 40 Трудового Кодекса РК работодатель не вправе требовать от работника выполнения работы, не обусловленной трудовым договором, за исключением случаев, предусмотренных настоящим Кодексом и законами Республики Казахстан. Таким случаем может быть совмещение должностей (расширение зоны обслуживания) и выполнение обязанностей временно отсутствующего работника. Согласно статьи 40-1 Трудового Кодекса РК работнику может быть поручено выполнение наряду с работой, определенной трудовым договором, дополнительной работы по другой или такой же должности за дополнительную оплату с его письменного согласия. Поручаемая работнику дополнительная работа по другой должности может осуществляться путем совмещения должностей. Поручаемая работнику дополнительная работа по такой же должности может осуществляться путем расширения зон обслуживания. Для исполнения обязанностей временно отсутствующего работника без освобождения от работы, определенной трудовым договором, работнику может быть поручена дополнительная работа как по другой, так и по такой же должности. Срок, в течение которого работник будет выполнять дополнительную работу, ее содержание и объем устанавливаются работодателем с письменного согласия работника. Работник имеет право досрочно отказаться от выполнения дополнительной работы, а работодатель – досрочно отменить поручение о ее выполнении, предупредив об этом другую сторону в письменной форме не позднее чем за три рабочих дня.'
    answers.user_id = 5
    answers.specialist_id = 2
    answers.save()

    answers = Answers()
    answers.id = 4
    answers.datea = datetime.now() - timedelta(days=15)
    answers.question = 'Можно ли оформлять имущестов на ребенка? Кто будет претендовать на это имущество в будущем?'
    answers.answer = 'В соответствии со статьей 66 Кодекса РК «О браке (супружестве) и семье», ребенок имеет право собственности на полученные им доходы, имущество, полученное им в дар или в порядке наследования, а также на любое другое имущество, приобретенное на его средства. Право ребенка на распоряжение принадлежащим ему на праве собственности имуществом определяется Гражданским кодексом Республики Казахстан. Возникновение у детей права собственности на имущество (движимое, недвижимое), не влечет возникновения права собственности на такое имущество у родителей. По достижении ребенком совершеннолетия, в отношении такого имущества родители будут иметь только права наследования в порядке первой очереди'
    answers.user_id = 6
    answers.specialist_id = 2
    answers.save()

    answers = Answers()
    answers.id = 5
    answers.datea = datetime.now() - timedelta(days=10)
    answers.question = 'Выезд в другое государство. Разрешение родителей'
    answers.answer = 'Правилами оформления документов на выезд за пределы Республики Казахстан на постоянное место жительства, утвержденными постановлением Правительства РК от 28 марта 2012 года № 361, одним из документов, необходимым для выезда на постоянное место жительства за пределы Республики Казахстан в органы внутренних дел по месту постоянного жительства гражданами Республики Казахстан лично или их законными представителями представляются — при выезде на постоянное место жительства граждан Республики Казахстан, не достигших восемнадцати лет, совместно с одним из родителей (опекуном, попечителем) — нотариально заверенное согласие другого родителя, проживающего на территории Республики Казахстан. При отсутствии согласия одного из родителей выезд несовершеннолетнего может быть разрешен в судебном порядке. В этом случае исковое заявление о разрешении выезда на ПМЖ за пределы РК без согласия другого родителя подается в суд по месту жительства родителя, не дающего согласия на выезд'
    answers.user_id = 7
    answers.specialist_id = 1
    answers.save()

    ##### Отзывы #####
    Reviews = apps.get_model("support", "reviews")
    
    reviews = Reviews()
    reviews.id = 1
    reviews.dater = '2021-11-01 12:00:00'
    reviews.details = 'За период оказания услуг Компания показала себя как надежный партнер, соблюдающий интересы своего клиента, с профессиональными и опытными кадрами. Компанией наряду с правовым сопровождением текущей деятельности были оказаны услуги по регистрации проспектов эмиссии ценных бумаг, регистрация Отчетов об итогах выпуска ценных бумаг в Агентстве по надзору деятельности финансового рынка и финансовых организаций.'
    reviews.user_id = 3
    reviews.save()

    reviews = Reviews()
    reviews.id = 2
    reviews.dater = '2021-11-02 12:00:00'
    reviews.details = ' целом работу отличает компетентность, заинтересованность в достижении и качестве конечного результат. Также считаем важным отметить, что юристы придерживаются высоких стандартов профессиональной этики и выстраивают взаимоотношения с клиентами, ориентируясь на долгосрочное сотрудничество...   '
    reviews.user_id = 4
    reviews.save()
        
    reviews = Reviews()
    reviews.id = 3
    reviews.dater = '2021-11-03 12:00:00'
    reviews.details = 'Основным преимуществом, на наш взгляд, является индивидуальный подход к требованиям клиента,  оперативность в сочетании с эффективностью, высокий уровень компетентности в своем деле. Нельзя не отметить, что представители компании  выполнили свою работу на высоком профессиональном уровне, в соответствии с условиями Договора, при этом проявив прекрасные личностные качества'
    reviews.user_id = 5
    reviews.save()
    
    reviews = Reviews()
    reviews.id = 4
    reviews.dater = '2021-11-04 12:00:00'
    reviews.details = 'Общественный фонд "Добровольное Общество "Милосердие" выражает Вам свое почтенние и благодарность за поддержку благотворительной акции "Подари детям жизнь". Ваша финансовая помощь станет вкладом в лечение детей с заболеваниями, неизлечимыми в Казахстане. Это неоценимая помощь детям в борьбе за здоровье!'
    reviews.user_id = 6
    reviews.save()
    
    reviews = Reviews()
    reviews.id = 5
    reviews.dater = '2021-11-05 12:00:00'
    reviews.details = 'За время сотрудничества компания показала себя как надежный партнер, а сотрудники неоднократно на практике подтверждали свой профессионализм и ответственный подход к любым вопросам. '
    reviews.user_id = 7
    reviews.save()

    ##### Галлерея #####
    
    Gallery = apps.get_model("support", "gallery")
   
    gallery = Gallery()
    gallery.id = 1
    gallery.dateg = '2021-11-01 12:00:00'
    gallery.title = 'Семинар на тему: Защита прав потребителей. Лектор: Клейман Ольга Сергеевна'
    gallery.details = ''
    gallery.photo = 'images/gallery1.jpeg'
    gallery.save()
   
    gallery = Gallery()
    gallery.id = 2
    gallery.dateg = '2021-11-02 12:00:00'
    gallery.title = 'Семинар на тему " Наследство по закону в Республике Казахстан" Лектор: Клейман Ольга Сергеевна'
    gallery.details = ''
    gallery.photo = 'images/gallery2.jpeg'
    gallery.save()
   
    gallery = Gallery()
    gallery.id = 3
    gallery.dateg = '2021-11-03 12:00:00'
    gallery.title = 'Обмен опыта во время обучения по программе подготовки профессиональных медиаторов.'
    gallery.details = ''
    gallery.photo = 'images/gallery3.jpeg'
    gallery.save()

    gallery = Gallery()
    gallery.id = 4
    gallery.dateg = '2021-11-04 12:00:00'
    gallery.title = 'Обмен опыта во время обучения по программе подготовки профессиональных медиаторов.'
    gallery.details = ''
    gallery.photo = 'images/gallery4.jpeg'
    gallery.save()

    gallery = Gallery()
    gallery.id = 5
    gallery.dateg = '2021-11-05 12:00:00'
    gallery.title = 'Постановка переговорного процесса во время обучения по программе подготовки профессиональных медиаторов.'
    gallery.details = ''
    gallery.photo = 'images/gallery5.jpeg'
    gallery.save()

class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(beginning),
    ]

