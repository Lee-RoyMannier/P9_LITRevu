from django import forms

from reviews.models import Ticket, Review


class TicketForm(forms.ModelForm):
    update_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Ticket
        exclude = ("user",)


class DeleteTicketForm(forms.Form):
    delete = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    update_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)]),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class DeleteReviewForm(forms.Form):
    delete = forms.BooleanField(widget=forms.HiddenInput, initial=True)
