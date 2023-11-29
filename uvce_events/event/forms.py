from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event, Student_Register

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    team_size = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2','team_size']


    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.extra_field = self.cleaned_data["team_size"]
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = "__all__"  

class Student_Register_Form(forms.ModelForm):
    class Meta:
        model = Student_Register
        fields = ['name', 'roll_number', 'email_address', 'branch', 'year']
        labels = {
            'branch': 'Select Branch',
            'year': 'Select Year',
        }




class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description','start_date', 'start_time', 'location', 'organizer']

    def __init__(self, *args, **kwargs):
        start_time = kwargs.pop('start_time', None)
        start_date = kwargs.pop('start_date', None)
        user = kwargs.pop('user', None)  # Get the user from the kwargs
        super(EventForm, self).__init__(*args, **kwargs)

        # Limit the queryset for the organizer field to only the logged-in user
        if user:
            self.fields['organizer'].queryset = User.objects.filter(pk=user.pk)
        
        # if start_time:
        #     self.fields['start_time'].initial = start_time
        # if start_date:
        #     self.fields['start_date'].initial = start_date  