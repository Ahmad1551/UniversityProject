#products views
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from config.mixins import PermissionRequiredMixin
from config.settings import DEFAULT_PAGINATION_SIZE
from projects.models import Organization, Product
from projects.forms import ProductForm


class ProductBaseView(PermissionRequiredMixin, View):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list_view')


class ProductListView(ProductBaseView, ListView):
    paginate_by = DEFAULT_PAGINATION_SIZE
    permission_required = 'projects.view_product'

    def get_queryset(self):
        organization_id = self.request.user.organization.id
        return Product.objects.filter(organization_id=organization_id)


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    success_url = reverse_lazy('product_list_view')
    form_class = ProductForm
    permission_required = 'projects.add_product'

    def form_valid(self, form):
        form.instance.organization = self.request.user.organization
        return super().form_valid(form)


class ProductDetailView(ProductBaseView, DetailView):
    permission_required = 'projects.view_product'


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy('product_list_view')
    form_class = ProductForm
    permission_required = 'projects.change_product'

    def form_valid(self, form):
        form.instance.organization = self.request.user.organization
        return super().form_valid(form)


class ProductDeleteView(ProductBaseView, DeleteView):
    permission_required = 'projects.delete_product'
