# eduquate

Образовательный сайт на Django.


## Структура проекта

Проект структурно разделен на 3 приложения: Accounts - отвечающий за профили, 
Courses - отвечающий за описание курсов на образовательной площадке и 
Learning - обслуживающий подписки пользователей на курсы. На данный момент
созданы только модели данных и доступна панель администратора.

### Модели данных. Accounts

В проекте предусмотрены 3 профиля: Студент, Преподаватель и Суперпользователь. 
Стандартный джанго-профиль заменен на собственный `User` и расширен
полями, общими для всех профилей, в качестве логина используется адрес электронной
почты. 

Профиль Студента является основным для системы и, поскольку пока полностью описывается
базовой пользовательской моделью, представлен в проекте прокси-моделью `Student`, которую 
при необходимости можно будет расширить связью один-к-одному с базовой.

Профиль Преподавателя `Tutor` является расширением базовой модели и представляет 
связь один-к-одному.

Суперпользователь - единственный профиль, которому будет доступна административная панель,
предполагается, что его можно создавать исключительно из консоли.

### Courses

Приложение представлено двумя связанными моделями (один-ко-многим): `Course` - 
описание курсов и `Lesson` - описание занятий в рамках курса. Помимо этого модель `Course`
связана с `Tutor` (многие-к-одному); предполагается, что преподаватели являются 
создателями и редакторами собственных курсов. Ещё одна связь `Course` - `Student` 
(многие-ко-многим) через промежуточную модель `learning.CourseSubscription`.

### Learning

Приложение представлено двумя моделями. `CourseSubscription` - промежуточная модель 
между курсом и студентом, хранящая дополнительные аттрибуты этой связи; предполагается,
что связь будет образовываться при подписке студента на произвольный курс, ограничивающим
фактором является невозможность преподавателя (автора курса) учится на собственном курсе.
`LearningProgress` - модель фиксирует прогресс обучения по занятиям в рамках ранее
созданной подписки.


## Установка и запуск

```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

TODO: запуск приложения из контейнера
