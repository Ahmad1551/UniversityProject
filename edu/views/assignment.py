from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from config.mixins import PermissionRequiredMixin
from config.settings import DEFAULT_PAGINATION_SIZE

from edu.models import Assignment


class AssignmentBaseView(PermissionRequiredMixin, View):
    model = Assignment
    fields = '__all__'
    success_url = reverse_lazy('assignment_list_view')


class AssignmentListView(AssignmentBaseView, ListView):
    paginate_by = DEFAULT_PAGINATION_SIZE


class AssignmentCreateView(AssignmentBaseView, CreateView):
    model = Assignment
    success_url = reverse_lazy('assignment_list_view')


class AssignmentDetailView(AssignmentBaseView, DetailView):
    permission_required = 'edu.view_plan'


class AssignmentUpdateView(AssignmentBaseView, UpdateView):
    model = Assignment
    success_url = reverse_lazy('assignment_list_view')



class AssignmentDeleteView(AssignmentBaseView, DeleteView):
    """Plan delete view."""
