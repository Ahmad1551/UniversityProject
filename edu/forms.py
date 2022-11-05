from django import forms

from edu.models import Bot, Plan, Subscription


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
        super(SubscriptionForm, self).__init__(*args, **kwargs)

        self.fields['is_active'].widget.attrs['class'] = 'form-check-input'


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)

        self.fields['is_active'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_popular'].widget.attrs['class'] = 'form-check-input'
