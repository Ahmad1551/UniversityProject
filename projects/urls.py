from django.urls import path

from projects.views.organization import (
    OrganizationListView, OrganizationCreateView, OrganizationDeleteView, OrganizationUpdateView, OrganizationDetailView
)
from projects.views.pdf import MyPDFView
from projects.views.product import (
    ProductListView, ProductCreateView, ProductDeleteView, ProductUpdateView, ProductDetailView
)

urlpatterns = [
    path('organizations/', OrganizationListView.as_view(), name='organization_list_view'),
    path('organizations/create/', OrganizationCreateView.as_view(), name='organization_create_view'),
    path('organizations/<int:pk>/', OrganizationDetailView.as_view(), name='organization_detail_view'),
    path('organizations/<int:pk>/update/', OrganizationUpdateView.as_view(), name='organization_update_view'),
    path('organizations/<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization_delete_view'),
    path('products/', ProductListView.as_view(), name='product_list_view'),
    path('products/create/', ProductCreateView.as_view(), name='product_create_view'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail_view'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update_view'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete_view'),
    path('pdf/', MyPDFView.as_view(), name='download_pdf'),
]
