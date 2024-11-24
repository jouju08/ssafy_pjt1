from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
url_name='accounts'

urlpatterns = [
     path('check-username/', views.check_username, name='check_username'),
     path('find-id/', views.find_id, name='find_id'),
     path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
     path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
     path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
     path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]