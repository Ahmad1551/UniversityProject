from django import forms

from core.models import User
from edu.models import Bot, Plan, Subscription
from projects.models import Organization


class BotForm(forms.ModelForm):
    class Meta:
        model = Bot
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BotForm, self).__init__(*args, **kwargs)

        self.fields['is_online'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_active'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_verified'].widget.attrs['class'] = 'form-check-input'


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        organization_id = kwargs.pop('organization_id')
        super(SubscriptionForm, self).__init__(*args, **kwargs)

        self.fields['plan'].queryset = Plan.objects.filter(organization_id=organization_id)
        self.fields['user'].queryset = User.objects.filter(organization_id=organization_id)
        self.fields['is_active'].widget.attrs['class'] = 'form-check-input'


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        organization_id = kwargs.pop('organization_id')
        super(PlanForm, self).__init__(*args, **kwargs)

        self.fields['organization'].queryset = Organization.objects.filter(id=organization_id)
        self.fields['is_active'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_popular'].widget.attrs['class'] = 'form-check-input'
