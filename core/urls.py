from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/status/<str:input>', views.status, name='status'),
]
