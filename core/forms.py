from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from core.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "username", "email", "password1", "password2", "phone_number", "user_type", "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['is_active'].widget.attrs['class'] = 'form-check-input'


class UpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "username", "email", "phone_number",
            "user_type", "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)

        self.fields['is_active'].widget.attrs['class'] = 'form-check-input'
