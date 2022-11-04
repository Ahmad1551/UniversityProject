from django.urls import path

from projects.views.organization import (
    OrganizationListView, OrganizationCreateView, OrganizationDeleteView, OrganizationUpdateView, OrganizationDetailView

)
from projects.views.pdf import MyPDFView


urlpatterns = [
    path('organizations/', OrganizationListView.as_view(), name='organization_list_view'),
    path('organizations/create/', OrganizationCreateView.as_view(), name='organization_create_view'),
    path('organizations/<int:pk>/', OrganizationDetailView.as_view(), name='organization_detail_view'),
    path('organizations/<int:pk>/update/', OrganizationUpdateView.as_view(), name='organization_update_view'),
    path('organizations/<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization_delete_view'),
    path('pdf/', MyPDFView.as_view(), name='download_pdf'),
]
