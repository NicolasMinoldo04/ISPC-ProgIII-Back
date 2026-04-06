from django.urls import path
from .views import RegisterView, LoginView
from .views import profile
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', profile),
]