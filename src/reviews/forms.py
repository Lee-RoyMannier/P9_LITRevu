from django import forms

from reviews.models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ("user",)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)]),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
