from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/check-password/<str:input>', views.check_password, name='check-password'),
    path('api/status', views.status, name='status'),
    path('change-password-view', views.change_password_view, name='change-password-view'),
    path('api/change-password/<str:input>', views.change_password, name='change-password'),
]
