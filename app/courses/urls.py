from django.urls import path

from courses import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='detail'),
    path('create/', views.CourseCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.CourseUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.CourseDelete.as_view(), name='delete'),
]