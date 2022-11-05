from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path('', include('edu.urls')),
    path('', include('projects.urls')),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login_view'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'config.views.handler404view'
handler500 = 'config.views.handler500view'
