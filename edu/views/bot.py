from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from config.mixins import PermissionRequiredMixin
from config.settings import DEFAULT_PAGINATION_SIZE
from edu.forms import BotForm
from edu.models import Bot
from projects.models import Organization


class BotBaseView(PermissionRequiredMixin, View):
    model = Bot
    fields = '__all__'
    success_url = reverse_lazy('bot_list_view')


class BotListView(BotBaseView, ListView):
    paginate_by = DEFAULT_PAGINATION_SIZE
    permission_required = 'edu.view_bot'


class BotCreateView(PermissionRequiredMixin, CreateView):
    model = Bot
    form_class = BotForm
    success_url = reverse_lazy('bot_list_view')
    permission_required = 'edu.add_bot'


class BotDetailView(BotBaseView, DetailView):
    permission_required = 'edu.view_bot'


class BotUpdateView(PermissionRequiredMixin, UpdateView):
    model = Bot
    form_class = BotForm
    success_url = reverse_lazy('bot_list_view')
    permission_required = 'edu.change_bot'


class BotDeleteView(BotBaseView, DeleteView):
    permission_required = 'edu.delete_bot'
