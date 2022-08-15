from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput, CharField


class RegisterForm(UserCreationForm):
    """
    Form for registering a new user, with no privileges, from the given username, email and
    password.
    """
    password1 = CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control", }),
    )
    password2 = CharField(
        label="Password confirmation",
        widget=PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control", }),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'John.D0e',
            }),
            'email': EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'your@mail.com',
                                       }),
        }

    def save(self, commit=True):
        user = super().save(commit=commit)
        return user
