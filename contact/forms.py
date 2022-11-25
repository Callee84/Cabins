from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': ('Enter your name')}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': ('Enter your email')}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': ('Enter a sbuject')}))
    question = forms.CharField(widget=forms.Textarea(attrs={'placeholder': ('Enter your question')}))
