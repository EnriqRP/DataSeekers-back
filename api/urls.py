from django.urls import path
from .views import UsersView

# Path for each action
urlpatterns = [
    path('users/', UsersView.as_view(), name='users_list'),
    path('users/<int:id>', UsersView.as_view(), name='users_process')
]
