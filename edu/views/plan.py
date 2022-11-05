from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from config.mixins import PermissionRequiredMixin
from config.settings import DEFAULT_PAGINATION_SIZE
from edu.forms import PlanForm
from edu.models import Plan


class PlanBaseView(PermissionRequiredMixin, View):
    model = Plan
    fields = '__all__'
    success_url = reverse_lazy('plan_list_view')


class PlanListView(PlanBaseView, ListView):
    paginate_by = DEFAULT_PAGINATION_SIZE
    permission_required = 'edu.view_plan'

    def get_queryset(self):
        return Plan.objects.filter(organization_id=self.request.user.organization.id)


class PlanCreateView(PermissionRequiredMixin, CreateView):
    model = Plan
    form_class = PlanForm
    success_url = reverse_lazy('plan_list_view')
    permission_required = 'edu.add_plan'

    def form_valid(self, form):
        form.instance.organization = self.request.user.organization
        return super().form_valid(form)


class PlanDetailView(PlanBaseView, DetailView):
    permission_required = 'edu.view_plan'


class PlanUpdateView(PermissionRequiredMixin, UpdateView):
    model = Plan
    form_class = PlanForm
    success_url = reverse_lazy('plan_list_view')
    permission_required = 'edu.change_plan'

    def form_valid(self, form):
        form.instance.organization = self.request.user.organization
        return super().form_valid(form)


class PlanDeleteView(PlanBaseView, DeleteView):
    permission_required = 'edu.delete_plan'
