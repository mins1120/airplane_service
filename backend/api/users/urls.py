from django.urls import path
from .views import SignupView, LoginView, DeleteUserView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('delete/<int:uid>/', DeleteUserView.as_view(), name='delete_user'),
]
