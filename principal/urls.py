from django.urls import path
from. import views


urlpatterns = [
    path('', views.Login, name='login'),
    path('yourname/<str:name>', views.yourname, name='yourname')
]
