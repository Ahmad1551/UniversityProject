from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from config.settings import DEFAULT_PAGINATION_SIZE
from config.mixins import PermissionRequiredMixin
from core.forms import RegisterForm, UpdateForm
from core.models import User


class UserBaseView(PermissionRequiredMixin, View):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('user_list_view')


class UserListView(UserBaseView, ListView):
    paginate_by = DEFAULT_PAGINATION_SIZE
    permission_required = 'core.view_user'

    def get_queryset(self):
        organization_id = self.request.user.organization.id
        return User.objects.filter(organization_id=organization_id)


class UserCreateView(PermissionRequiredMixin, CreateView):
    model = User
    success_url = reverse_lazy('user_list_view')
    form_class = RegisterForm
    permission_required = 'core.add_user'

    def form_valid(self, form):
        form.instance.organization = self.request.user.organization
        return super().form_valid(form)


class UserDetailView(UserBaseView, DetailView):
    permission_required = 'core.view_user'


class UserUpdateView(PermissionRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('user_list_view')
    form_class = UpdateForm
    permission_required = 'core.change_user'


class UserDeleteView(UserBaseView, DeleteView):
    permission_required = 'core.delete_user'
