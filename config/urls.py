from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path("login/", auth_views.LoginView.as_view(), name="login_view"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout_view"),
]
