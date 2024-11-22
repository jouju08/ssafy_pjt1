from django.urls import path
from . import views 

url_name='accounts'

urlpatterns = [
     path('check-username/', views.check_username, name='check_username'),
]