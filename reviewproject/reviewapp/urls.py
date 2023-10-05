from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('write', views.write, name='write'),
    path('show', views.show, name='show'),
    path('table', views.table_cmd, name='table_cmd'),
    path('fl', views.fl, name='fl'),
    path('fldata', views.fldata, name='fldata'),
]
