from django import forms

SUBJECT_CHOICES = (
    (1, 'Inquiry Sälen'),
    (2, 'Inquiry Öland'),
    (3, 'Question'),
)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES,
    )
    question = forms.CharField(widget=forms.Textarea)
