from django import forms
class ArticleForm(forms.Form):
    title = forms.CharField(label="Name", max_length=100)
    content = forms.CharField(label="Content", widget=forms.Textarea)


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]