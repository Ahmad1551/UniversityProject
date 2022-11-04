from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from config.mixins import PermissionRequiredMixin
from config.settings import DEFAULT_PAGINATION_SIZE
from projects.models import Organization


class OrganizationBaseView(PermissionRequiredMixin, View):
    model = Organization
    fields = '__all__'
    success_url = reverse_lazy('organization_list_view')


class OrganizationListView(OrganizationBaseView, ListView):
    paginate_by = DEFAULT_PAGINATION_SIZE
    permission_required = 'prejects.view_organization'


class OrganizationCreateView(OrganizationBaseView, CreateView):
    permission_required = 'projects.add_organization'


class OrganizationDetailView(OrganizationBaseView, DetailView):
    permission_required = 'prejects.view_organization'


class OrganizationUpdateView(OrganizationBaseView, UpdateView):
    permission_required = 'prejects.change_organization'


class OrganizationDeleteView(OrganizationBaseView, DeleteView):
    permission_required = 'prejects.delete_organization'
