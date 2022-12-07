from django import forms
from .models import PostGuest, Category


choices = Category.objects.all().values_list('name', 'name')

cabin_choice = []

for cabin in choices:
    cabin_choice.append(cabin)


class AddGuestPost(forms.ModelForm):
    # form for writing review i guestbook
    class Meta:
        model = PostGuest
        fields = ('title', 'author', 'category', 'content')

        widgets = {
            'title': forms.TextInput,
            'author': forms.TextInput(
                attrs={'value': '', 'id': 'user_id', 'type': 'hidden'}),
            'category': forms.Select(choices=cabin_choice),
            'content': forms.Textarea,
        }
