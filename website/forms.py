from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ZooUser, ZooBooking

from django import forms 
from django.forms.widgets import PasswordInput, TextInput, EmailInput

# Register
class CreateUserForm(UserCreationForm):

    class Meta:
        model = ZooUser
        fields = ['username', 'email', 'password1', 'password2']

# Login 
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    email = forms.CharField(widget=EmailInput())

class Zoo_Booking_Form(forms.ModelForm):

    class Meta:
        model = ZooBooking

        fields = ['zoo_booking_date_arrive', 'zoo_booking_adults', 'zoo_booking_children','zoo_booking_oap']

        labels = {
            "zoo_booking_date_arrive": 'day you wish to arrive?',
        }

        widgets = {
            'zoo_booking_date_arrive': forms.DateInput(attrs={'type': 'date'}),
            'zoo_total_cost': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)