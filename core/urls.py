from django.urls import path

from core.views.dashboard import DashboardTemplateView
from core.views.users import (
    UserListView, UserCreateView, UserDetailView, UserUpdateView, UserDeleteView
)

urlpatterns = [
    path('', DashboardTemplateView.as_view(), name="dashboard_view"),
    path('users/', UserListView.as_view(), name='user_list_view'),
    path('users/create/', UserCreateView.as_view(), name='user_create_view'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail_view'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update_view'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete_view'),
]
