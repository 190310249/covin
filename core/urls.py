from django.urls import path
from .import views


urlpatterns = [
    path('oauth2/', views.oauth2, name='oauth2'),
    path('oauth2/success', views.oauth2_success, name='oauth2_success')
]
