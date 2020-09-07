from django.urls import path
from . import views

urlpatterns = [
    # path("", views.accounts_login, name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]