from django.urls import path

from books.views.dashboard import DashboardTemplateView

urlpatterns = [
    path('', DashboardTemplateView.as_view(), name="dashboard_view"),
]
