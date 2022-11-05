from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

from edu.views.chegg import CheggView

urlpatterns = [
    path('chegg/', CheggView.as_view(), name='chegg_view'),
]
