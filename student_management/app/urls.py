from django.urls import path
from app import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.home, name = 'home'),
    path('sign-up/', views.signup, name='signup'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('catalog/', views.display_catalog, name = 'catalog'),
    path('enroll/', views.enroll, name = 'enroll'),
    path('add_course/', views.add_course, name = 'add_course'),
    path('edit_course/', views.edit_course, name = 'edit_course'),
]
