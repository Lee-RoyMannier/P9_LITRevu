from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()
class FollowingForm(forms.Form):
    following = forms.CharField(
        label="Username",
        widget=forms.TextInput(),
        required=False,
    )

    def clean_user_id(self):
        user = self.cleaned_data.get("following")
        if not user:
            raise forms.ValidationError("A valid Username is required.")
        return user

