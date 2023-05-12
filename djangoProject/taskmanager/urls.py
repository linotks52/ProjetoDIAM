from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .converters import IntArrayConverter
from django.urls import register_converter

register_converter(IntArrayConverter, 'int_array')

app_name = 'taskmanager'
urlpatterns = [
                  path('tasks/', views.task_list, name='task_list'),
                  path('tasks/create/', views.create_task, name='create_task'),
                  path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
                  path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
                  path('signup', views.signup, name='signup'),
                  path('', views.logar, name='logar'),
                  path('tasks/delete/<int_array:ids>/', views.multiple_delete, name='multiple_delete'),
                  path("profile/", views.profile, name='profile'),
                  path("profile/edit_profile/", views.edit_profile, name='edit_profile'),
                  path("sair", views.sair, name='sair'),
                  path("creditos", views.creditos, name='creditos')
              ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
