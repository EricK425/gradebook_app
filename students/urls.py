from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # students/eric/kleihege/
    path('<str:student_first_name>/<str:student_last_name>/', views.detail, name='detail'),
    # students/eric/kleihege/update/
    path('<str:student_first_name>/<str:student_last_name>/update/', views.update, name='update'),
]
