import datetime

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from config.mixins import PermissionRequiredMixin
from config.settings import DEFAULT_PAGINATION_SIZE
from edu.forms import SubscriptionForm
from edu.models import Subscription


class SubscriptionBaseView(PermissionRequiredMixin, View):
    model = Subscription
    fields = '__all__'
    success_url = reverse_lazy('subscription_list_view')


class SubscriptionListView(SubscriptionBaseView, ListView):
    paginate_by = DEFAULT_PAGINATION_SIZE
    permission_required = 'edu.view_subscription'

    def get_queryset(self):
        return Subscription.objects.filter(plan__organization_id=self.request.user.organization.id)


class SubscriptionCreateView(PermissionRequiredMixin, CreateView):
    model = Subscription
    form_class = SubscriptionForm
    success_url = reverse_lazy('subscription_list_view')
    permission_required = 'edu.add_subscription'

    def get_form_kwargs(self):
        kwargs = super(SubscriptionCreateView, self).get_form_kwargs()
        kwargs['organization_id'] = self.request.user.organization_id
        return kwargs

    def form_valid(self, form):
        validity_months = form.cleaned_data['plan'].duration
        form.instance.end_date = datetime.date.today() + datetime.timedelta(days=validity_months * 30)
        return super().form_valid(form)


class SubscriptionDetailView(SubscriptionBaseView, DetailView):
    permission_required = 'edu.view_subscription'


class SubscriptionUpdateView(PermissionRequiredMixin, UpdateView):
    model = Subscription
    form_class = SubscriptionForm
    success_url = reverse_lazy('subscription_list_view')
    permission_required = 'edu.change_subscription'

    def get_form_kwargs(self):
        kwargs = super(SubscriptionCreateView, self).get_form_kwargs()
        kwargs['organization_id'] = self.request.user.organization_id
        return kwargs

    def form_valid(self, form):
        validity_months = form.cleaned_data['plan'].duration
        form.instance.end_date = datetime.date.today() + datetime.timedelta(days=validity_months * 30)
        return super().form_valid(form)


class SubscriptionDeleteView(SubscriptionBaseView, DeleteView):
    permission_required = 'edu.delete_subscription'
